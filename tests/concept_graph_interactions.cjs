// Offline interaction tests: execute the shipped script against a small SVG DOM.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const source = fs.readFileSync(path.join(__dirname, "../assets/js/concept-graph.js"), "utf8");

async function graph(scaleX = 0.5, scaleY = 0.75) {
  const captured = new Map();
  const opened = [];
  const document = { activeElement: null };
  class Element {
    constructor(tag) {
      this.tag = tag;
      this.attributes = {};
      this.children = [];
      this.listeners = {};
      const classes = new Set();
      this.classList = {
        add: (...names) => names.forEach((name) => classes.add(name)),
        remove: (name) => classes.delete(name),
        contains: (name) => classes.has(name),
      };
    }
    setAttribute(name, value) {
      this.attributes[name] = String(value);
      if (name === "class") this.classList.add(...value.split(" "));
    }
    getAttribute(name) { return this.attributes[name] ?? null; }
    appendChild(child) { child.parent = this; this.children.push(child); }
    contains(child) { return child === this || this.children.some((item) => item.contains(child)); }
    matches(selector) {
      if (selector.startsWith(".")) return this.classList.contains(selector.slice(1));
      if (selector.startsWith("#")) return this.getAttribute("id") === selector.slice(1);
      return this.tag === selector;
    }
    closest(selector) { return this.matches(selector) ? this : this.parent?.closest(selector); }
    querySelectorAll(selector) {
      return this.children.flatMap((child) => [
        ...(child.matches(selector) ? [child] : []), ...child.querySelectorAll(selector),
      ]);
    }
    querySelector(selector) { return this.querySelectorAll(selector)[0] || null; }
    set innerHTML(html) {
      this.html = html;
      this.children.forEach((child) => { child.parent = null; });
      this.children = [];
      // Only filters and the details link need parsed children in these tests.
      if (html.includes("<input")) this.appendChild(new Element("input"));
      if (html.includes("<a ")) this.appendChild(new Element("a"));
    }
    get innerHTML() { return this.html; }
    addEventListener(type, listener) { (this.listeners[type] ||= []).push(listener); }
    focus() { document.activeElement = this; }
    setPointerCapture(id) { captured.set(id, this); }
    hasPointerCapture(id) { return captured.get(id) === this; }
    releasePointerCapture(id) {
      captured.delete(id);
      fire(this, "lostpointercapture", { pointerId: id });
    }
  }
  const body = new Element("body");
  for (const id of ["concept-graph", "graph-details", "graph-search", "graph-layout",
    "graph-depth", "graph-reset", "graph-type-filters", "graph-edge-filters"]) {
    const element = new Element(id === "concept-graph" ? "svg" : "div");
    element.setAttribute("id", id);
    body.appendChild(element);
  }
  document.getElementById = (id) => body.querySelector(`#${id}`);
  document.createElement = document.createElementNS = (...args) => new Element(args.at(-1));
  const svg = document.getElementById("concept-graph");
  // Include a screen offset and unequal scales to detect client/SVG unit mixing.
  svg.getScreenCTM = () => ({ inverse: () => ({
    a: 1 / scaleX, b: 0, c: 0, d: 1 / scaleY, e: -30 / scaleX, f: -70 / scaleY,
  }) });
  svg.createSVGPoint = () => ({ x: 0, y: 0, matrixTransform(m) {
    return { x: m.a * this.x + m.c * this.y + m.e, y: m.b * this.x + m.d * this.y + m.f };
  } });
  const data = {
    nodes: [{ id: "example", title: "Example", type: "definition", url: "/math/incerto/example/" }],
    edges: [],
    layouts: { dag: { width: 920, height: 620, nodes: { example: { x: 100, y: 150 } } } },
    stats: { node_count: 1, dependency_edge_count: 0, reference_edge_count: 0 },
  };
  function fire(target, type, values = {}) {
    const event = { type, button: 0, isPrimary: true, pointerId: 1, pointerType: "mouse",
      clientX: 100, clientY: 150, ...values,
      preventDefault() { this.defaultPrevented = true; },
      stopPropagation() { this.stopped = true; },
    };
    event.target = type.startsWith("pointer") ? (captured.get(event.pointerId) || target) : target;
    for (let current = event.target; current; current = current.parent) {
      for (const listener of current.listeners[type] || []) listener(event);
      if (event.stopped) break;
    }
    return event;
  }
  vm.runInNewContext(source, {
    document, window: { open: (...args) => opened.push(args), addEventListener() {} },
    fetch: async () => ({ ok: true, json: async () => data }),
  });
  await new Promise(setImmediate);
  assert.ok(svg.querySelector(".node"), document.getElementById("graph-details").innerHTML);
  const transform = () => document.getElementById("graph-viewport").getAttribute("transform")
    .match(/-?\d+(?:\.\d+)?(?:e[+-]?\d+)?/gi).map(Number);
  return { svg, document, body, fire, captured, opened, transform, node: () => svg.querySelector(".node") };
}

function close(actual, expected) { assert.ok(Math.abs(actual - expected) < 1e-9, `${actual} != ${expected}`); }

for (const scale of [0.5, 2]) {
  test(`pan follows screen motion at SVG scale ${scale}, including after zoom`, async () => {
    const g = await graph(scale, scale * 1.5);
    g.fire(g.svg, "wheel", { deltaY: -1 });
    const [x, y, k] = g.transform();
    close(k, 1.1);
    g.fire(g.svg, "pointerdown");
    assert.equal(g.captured.get(1), g.svg);
    g.fire(g.body, "pointermove", { clientX: 130, clientY: 120 });
    close(g.transform()[0], x + 30 / scale);
    close(g.transform()[1], y - 30 / (scale * 1.5));
    // Capture stays on the SVG even though each move replaces its children.
    g.fire(g.body, "pointermove", { clientX: 160, clientY: 180 });
    close(g.transform()[0], x + 60 / scale);
    close(g.transform()[1], y + 30 / (scale * 1.5));
    g.fire(g.body, "pointerup");
    assert.equal(g.captured.size, 0);
    assert.equal(g.svg.classList.contains("is-dragging"), false);
    const ended = g.transform();
    g.fire(g.svg, "pointermove", { clientX: 300 });
    assert.deepEqual(g.transform(), ended);
  });
}

for (const pointerType of ["mouse", "touch", "pen"]) {
  test(`${pointerType} can drag a node through the zoomed screen transform`, async () => {
    const g = await graph();
    g.fire(g.svg, "wheel", { deltaY: -1 });
    const [x, y, k] = g.transform();
    g.fire(g.node().querySelector("circle"), "pointerdown", { pointerType });
    assert.equal(g.captured.get(1), g.svg);
    g.fire(g.body, "pointermove", { pointerType, clientX: 140, clientY: 190 });
    const point = g.node().getAttribute("transform").match(/-?\d+(?:\.\d+)?/g).map(Number);
    close(point[0], ((140 - 30) / 0.5 - x) / k);
    close(point[1], ((190 - 70) / 0.75 - y) / k);
    assert.deepEqual(g.transform(), [x, y, k]);
    g.fire(g.body, "pointerup", { pointerType });
    assert.equal(g.captured.size, 0);
  });
}

test("only the active primary pointer controls a gesture; cancellation releases it", async () => {
  const g = await graph();
  g.fire(g.svg, "pointerdown", { button: 2 });
  g.fire(g.svg, "pointerdown", { isPrimary: false, pointerId: 2 });
  assert.equal(g.captured.size, 0);
  g.fire(g.svg, "pointerdown", { pointerType: "touch" });
  g.fire(g.node(), "pointerdown", { pointerId: 2 });
  g.fire(g.svg, "pointermove", { pointerId: 2, clientX: 400 });
  g.fire(g.svg, "pointerup", { pointerId: 2 });
  assert.deepEqual(g.transform(), [0, 0, 1]);
  assert.equal(g.captured.get(1), g.svg);
  g.fire(g.svg, "pointercancel", { pointerType: "touch" });
  assert.equal(g.captured.size, 0);
  assert.equal(g.svg.classList.contains("is-dragging"), false);
  g.fire(g.node(), "pointerdown", { pointerType: "touch" });
  g.fire(g.svg, "pointercancel", { pointerType: "touch" });
  assert.equal(g.node().getAttribute("aria-pressed"), "false");
  g.fire(g.svg, "pointerdown");
  g.svg.releasePointerCapture(1);
  g.fire(g.svg, "pointermove", { clientX: 400 });
  assert.deepEqual(g.transform(), [0, 0, 1]);
  assert.equal(g.svg.classList.contains("is-dragging"), false);
});

test("touch taps, keyboard selection/focus, and double-click navigation remain usable", async () => {
  const g = await graph();
  g.fire(g.node(), "pointerdown", { pointerType: "touch" });
  g.fire(g.svg, "pointerup", { pointerType: "touch" });
  assert.equal(g.node().getAttribute("aria-pressed"), "true");
  for (const key of ["Enter", " "]) {
    g.fire(g.document.getElementById("graph-reset"), "click");
    g.node().focus();
    const event = g.fire(g.node(), "keydown", { key });
    assert.equal(event.defaultPrevented, true);
    assert.equal(g.node().getAttribute("aria-pressed"), "true");
    assert.equal(g.document.activeElement, g.node());
    assert.ok(g.document.getElementById("graph-details").querySelector("a"));
  }
  // Pointer capture may retarget dblclick to the root; hit-testing finds the node.
  g.document.elementFromPoint = () => g.node().querySelector("circle");
  g.fire(g.svg, "dblclick");
  assert.deepEqual(g.opened, [["/math/incerto/example/", "_parent"]]);
  g.document.elementFromPoint = () => g.svg;
  g.fire(g.svg, "dblclick");
  assert.equal(g.opened.length, 1);
});
