  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg:       #0f1117;
    --surface:  #1a1f2e;
    --surface2: #212840;
    --border:   #2a3050;
    --text:     #e2e8f0;
    --muted:    #8892a4;
    --dim:      #4a5568;
    --blue:     #60a5fa;
    --blue-bg:  #1e3a5f;
    --green:    #4ade80;
    --green-bg: #14532d;
    --orange:   #fb923c;
    --orange-bg:#431407;
    --purple:   #c084fc;
    --purple-bg:#3b1f6e;
    --yellow:   #fbbf24;
    --red:      #f87171;
  }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', system-ui, sans-serif;
    font-size: 12px;
    line-height: 1.5;
    padding: 20px;
    max-width: 1100px;
    margin: 0 auto;
  }

  /*  Header  */
  .header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 2px solid var(--blue);
    padding-bottom: 10px;
    margin-bottom: 16px;
  }
  .header h1 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    font-weight: 600;
    color: var(--blue);
    letter-spacing: -0.5px;
  }
  .header .tagline {
    font-size: 11px;
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
  }

  /*  Layout  */
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
  }
  .span2 { grid-column: span 2; }
  .span3 { grid-column: span 3; }

  /*  Cards  */
  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 14px;
  }
  .card-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 10px;
    padding-bottom: 6px;
    border-bottom: 1px solid var(--border);
  }
  .blue   .card-title { color: var(--blue);   border-color: var(--blue-bg); }
  .green  .card-title { color: var(--green);  border-color: var(--green-bg); }
  .orange .card-title { color: var(--orange); border-color: var(--orange-bg); }
  .purple .card-title { color: var(--purple); border-color: var(--purple-bg); }
  .yellow .card-title { color: var(--yellow); }

  /*  SVS Diagram  */
  .svs-diagram {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
  .svs-outer {
    border: 1.5px dashed var(--blue);
    border-radius: 8px;
    padding: 8px 10px;
    position: relative;
  }
  .svs-label {
    position: absolute;
    top: -9px;
    left: 10px;
    background: var(--surface);
    padding: 0 6px;
    font-size: 9px;
    font-family: 'JetBrains Mono', monospace;
    color: var(--blue);
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }
  .svs-row {
    display: flex;
    gap: 6px;
    align-items: center;
  }
  .svs-box {
    flex: 1;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 5px;
    padding: 5px 8px;
    text-align: center;
    font-size: 10px;
    font-weight: 600;
  }
  .svs-box.input  { background: var(--blue-bg);   border-color: var(--blue);   color: var(--blue); flex: 0 0 70px; }
  .svs-box.output { background: var(--green-bg);  border-color: var(--green);  color: var(--green); flex: 0 0 70px; }
  .svs-box.gp    { background: var(--orange-bg); border-color: var(--orange); color: var(--orange); }
  .svs-box.svc   { background: var(--blue-bg);   border-color: var(--blue);   color: var(--blue); }
  .svs-box.pr    { background: var(--purple-bg); border-color: var(--purple); color: var(--purple); }
  .svs-box.cont  { background: var(--surface2);  color: var(--muted); font-size: 9px; }
  .arrow {
    color: var(--muted);
    font-size: 14px;
    flex-shrink: 0;
  }
  .svs-subtitle { font-size: 9px; color: var(--muted); margin-top: 2px; font-weight: 400; }

  /*  SVC Chain  */
  .svc-chain {
    display: flex;
    align-items: stretch;
    gap: 0;
    margin-top: 4px;
  }
  .svc-step {
    flex: 1;
    background: var(--surface2);
    border: 1px solid var(--border);
    padding: 7px 5px;
    text-align: center;
    font-size: 10px;
    font-weight: 600;
    color: var(--blue);
    position: relative;
    line-height: 1.3;
  }
  .svc-step:not(:last-child)::after {
    content: '›';
    position: absolute;
    right: -7px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--muted);
    font-size: 14px;
    z-index: 1;
  }
  .svc-step:first-child { border-radius: 5px 0 0 5px; }
  .svc-step:last-child  { border-radius: 0 5px 5px 0; }
  .svc-step .sub { font-size: 9px; color: var(--muted); font-weight: 400; margin-top: 2px; }
  .svc-improve {
    text-align: center;
    font-size: 10px;
    color: var(--green);
    margin-top: 6px;
    padding: 4px;
    background: var(--green-bg);
    border-radius: 4px;
    border: 1px dashed var(--green);
    font-weight: 600;
  }

  /*  Dimensions  */
  .dims {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
  }
  .dim-box {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 5px;
    padding: 7px 9px;
  }
  .dim-icon { font-size: 16px; display: block; margin-bottom: 3px; }
  .dim-name { font-size: 10px; font-weight: 700; color: var(--text); }
  .dim-q    { font-size: 10px; color: var(--muted); margin-top: 2px; }

  /*  Bullet lists  */
  ul { list-style: none; }
  ul li {
    padding: 3px 0;
    padding-left: 14px;
    position: relative;
    font-size: 11px;
    color: var(--text);
  }
  ul li::before {
    content: '›';
    position: absolute;
    left: 0;
    color: var(--muted);
  }
  ul li strong { font-weight: 600; }
  ul li .eg { color: var(--muted); font-style: italic; }

  /*  Principles grid  */
  .principles {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5px;
  }
  .principle {
    background: var(--surface2);
    border-left: 2px solid var(--orange);
    border-radius: 0 4px 4px 0;
    padding: 5px 8px;
    font-size: 10px;
  }
  .principle strong { color: var(--orange); display: block; font-size: 10px; margin-bottom: 1px; }
  .principle span   { color: var(--muted); font-size: 10px; }

  /*  Practices grid  */
  .practices {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5px;
  }
  .practice {
    background: var(--surface2);
    border-left: 2px solid var(--purple);
    border-radius: 0 4px 4px 0;
    padding: 5px 8px;
  }
  .practice .pname { font-size: 10px; font-weight: 600; color: var(--purple); }
  .practice .pdesc { font-size: 10px; color: var(--muted); margin-top: 1px; }

  /*  Key terms  */
  .terms {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 5px;
  }
  .term {
    background: var(--surface2);
    border-radius: 4px;
    padding: 6px 8px;
  }
  .term .tname { font-size: 10px; font-weight: 700; color: var(--yellow); }
  .term .tdef  { font-size: 10px; color: var(--muted); margin-top: 2px; }

  /*  Incident vs Problem  */
  .compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-top: 4px;
  }
  .compare-box {
    background: var(--surface2);
    border-radius: 5px;
    padding: 7px 9px;
  }
  .compare-box .clabel { font-size: 10px; font-weight: 700; margin-bottom: 4px; }
  .compare-box.inc .clabel { color: var(--red); }
  .compare-box.prb .clabel { color: var(--orange); }
  .compare-box p { font-size: 10px; color: var(--muted); }
  .compare-box .eg { font-size: 10px; color: var(--text); margin-top: 4px; font-style: italic; }

  /*  Footer  */
  .footer {
    margin-top: 14px;
    padding-top: 10px;
    border-top: 1px solid var(--border);
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--dim);
    display: flex;
    justify-content: space-between;
  }