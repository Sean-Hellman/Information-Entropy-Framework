<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <!-- Gradients -->
    <linearGradient id="quantumGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3a0ca3" />
      <stop offset="100%" stop-color="#4361ee" />
    </linearGradient>
    <linearGradient id="spacetimeGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4cc9f0" />
      <stop offset="100%" stop-color="#4895ef" />
    </linearGradient>
    <linearGradient id="macroGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f72585" />
      <stop offset="100%" stop-color="#b5179e" />
    </linearGradient>
    
    <!-- Filters for glow effects -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    
    <!-- Animation definitions -->
    <animate id="pulseAnimation" attributeName="r" from="3" to="6" dur="2s" begin="0s" repeatCount="indefinite" />
    
    <!-- Patterns for backgrounds -->
    <pattern id="gridPattern" patternUnits="userSpaceOnUse" width="20" height="20" patternTransform="rotate(45)">
      <path d="M 0 0 L 0 20 M 0 0 L 20 0" stroke="#4361ee20" stroke-width="1" />
    </pattern>
  </defs>
  
  <!-- Background -->
  <rect width="800" height="600" fill="#050A30" />
  <rect width="800" height="600" fill="url(#gridPattern)" />
  
  <!-- Title -->
  <text x="400" y="40" font-family="Arial, sans-serif" font-size="24" fill="white" text-anchor="middle" font-weight="bold">The Information-Entropy Framework</text>
  <text x="400" y="70" font-family="Arial, sans-serif" font-size="16" fill="#8ecae6" text-anchor="middle">From Quantum Information to Emergent Spacetime</text>
  
  <!-- Quantum Information Layer (Bottom) -->
  <g id="quantumLayer" transform="translate(0, 500)">
    <rect x="50" y="-80" width="700" height="100" rx="10" fill="url(#quantumGradient)" opacity="0.2" />
    <text x="400" y="-30" font-family="Arial, sans-serif" font-size="16" fill="white" text-anchor="middle">Quantum Information Substrate</text>
    
    <!-- Quantum network nodes and connections -->
    <g id="quantumNetwork">
      <!-- Animated quantum nodes with pulsing -->
      <g id="quantumNodes">
        <circle id="node1" cx="100" cy="-50" r="4" fill="white">
          <animate attributeName="r" from="3" to="5" dur="2s" begin="0s" repeatCount="indefinite" />
          <animate attributeName="opacity" from="1" to="0.5" dur="3s" begin="0s" repeatCount="indefinite" />
        </circle>
        <circle id="node2" cx="180" cy="-60" r="4" fill="white">
          <animate attributeName="r" from="3" to="5" dur="2s" begin="0.3s" repeatCount="indefinite" />
          <animate attributeName="opacity" from="1" to="0.5" dur="3s" begin="0.3s" repeatCount="indefinite" />
        </circle>
        <circle id="node3" cx="250" cy="-40" r="4" fill="white">
          <animate attributeName="r" from="3" to="5" dur="2s" begin="0.6s" repeatCount="indefinite" />
          <animate attributeName="opacity" from="1" to="0.5" dur="3s" begin="0.6s" repeatCount="indefinite" />
        </circle>
        <circle id="node4" cx="310" cy="-60" r="4" fill="white">
          <animate attributeName="r" from="3" to="5" dur="2s" begin="0.9s" repeatCount="indefinite" />
          <animate attributeName="opacity" from="1" to="0.5" dur="3s" begin="0.9s" repeatCount="indefinite" />
        </circle>
        <circle id="node5" cx="380" cy="-30" r="4" fill="white">
          <animate attributeName="r" from="3" to="5" dur="2s" begin="1.2s" repeatCount="indefinite" />
          <animate attributeName="opacity" from="1" to="0.5" dur="3s" begin="1.2s" repeatCount="indefinite" />
        </circle>
        <circle id="node6" cx="460" cy="-50" r="4" fill="white">
          <animate attributeName="r" from="3" to="5" dur="2s" begin="1.5s" repeatCount="indefinite" />
          <animate attributeName="opacity" from="1" to="0.5" dur="3s" begin="1.5s" repeatCount="indefinite" />
        </circle>
        <circle id="node7" cx="530" cy="-40" r="4" fill="white">
          <animate attributeName="r" from="3" to="5" dur="2s" begin="1.8s" repeatCount="indefinite" />
          <animate attributeName="opacity" from="1" to="0.5" dur="3s" begin="1.8s" repeatCount="indefinite" />
        </circle>
        <circle id="node8" cx="600" cy="-60" r="4" fill="white">
          <animate attributeName="r" from="3" to="5" dur="2s" begin="2.1s" repeatCount="indefinite" />
          <animate attributeName="opacity" from="1" to="0.5" dur="3s" begin="2.1s" repeatCount="indefinite" />
        </circle>
        <circle id="node9" cx="650" cy="-30" r="4" fill="white">
          <animate attributeName="r" from="3" to="5" dur="2s" begin="2.4s" repeatCount="indefinite" />
          <animate attributeName="opacity" from="1" to="0.5" dur="3s" begin="2.4s" repeatCount="indefinite" />
        </circle>
      </g>
      
      <!-- Quantum entanglement connections (animated) -->
      <g id="quantumConnections" stroke="white" stroke-width="1" opacity="0.5">
        <line x1="100" y1="-50" x2="180" y2="-60">
          <animate attributeName="opacity" from="0.2" to="0.7" dur="4s" begin="0s" repeatCount="indefinite" />
        </line>
        <line x1="180" y1="-60" x2="250" y2="-40">
          <animate attributeName="opacity" from="0.2" to="0.7" dur="4s" begin="0.4s" repeatCount="indefinite" />
        </line>
        <line x1="250" y1="-40" x2="310" y2="-60">
          <animate attributeName="opacity" from="0.2" to="0.7" dur="4s" begin="0.8s" repeatCount="indefinite" />
        </line>
        <line x1="310" y1="-60" x2="380" y2="-30">
          <animate attributeName="opacity" from="0.2" to="0.7" dur="4s" begin="1.2s" repeatCount="indefinite" />
        </line>
        <line x1="380" y1="-30" x2="460" y2="-50">
          <animate attributeName="opacity" from="0.2" to="0.7" dur="4s" begin="1.6s" repeatCount="indefinite" />
        </line>
        <line x1="460" y1="-50" x2="530" y2="-40">
          <animate attributeName="opacity" from="0.2" to="0.7" dur="4s" begin="2.0s" repeatCount="indefinite" />
        </line>
        <line x1="530" y1="-40" x2="600" y2="-60">
          <animate attributeName="opacity" from="0.2" to="0.7" dur="4s" begin="2.4s" repeatCount="indefinite" />
        </line>
        <line x1="600" y1="-60" x2="650" y2="-30">
          <animate attributeName="opacity" from="0.2" to="0.7" dur="4s" begin="2.8s" repeatCount="indefinite" />
        </line>
        <!-- Cross connections -->
        <line x1="180" y1="-60" x2="380" y2="-30">
          <animate attributeName="opacity" from="0.1" to="0.4" dur="5s" begin="1.0s" repeatCount="indefinite" />
        </line>
        <line x1="250" y1="-40" x2="460" y2="-50">
          <animate attributeName="opacity" from="0.1" to="0.4" dur="5s" begin="2.0s" repeatCount="indefinite" />
        </line>
        <line x1="310" y1="-60" x2="530" y2="-40">
          <animate attributeName="opacity" from="0.1" to="0.4" dur="5s" begin="3.0s" repeatCount="indefinite" />
        </line>
      </g>
      
      <!-- Entropy formula -->
      <text x="100" y="-10" font-family="Arial, sans-serif" font-size="12" fill="#8ecae6" text-anchor="start">
        S<tspan baseline-shift="sub" font-size="8">vN</tspan> = -Tr(ρ log ρ)
      </text>
      
      <!-- Planck scale indicator -->
      <text x="650" y="-10" font-family="Arial, sans-serif" font-size="12" fill="#8ecae6" text-anchor="end">
        Planck Scale (10<tspan baseline-shift="super" font-size="8">-35</tspan> m)
      </text>
    </g>
  </g>
  
  <!-- Emergent Spacetime Layer (Middle) -->
  <g id="spacetimeLayer" transform="translate(0, 300)">
    <rect x="50" y="-80" width="700" height="100" rx="10" fill="url(#spacetimeGradient)" opacity="0.2" />
    <text x="400" y="-30" font-family="Arial, sans-serif" font-size="16" fill="white" text-anchor="middle">Emergent Spacetime Geometry</text>
    
    <!-- Spacetime grid with curvature -->
    <g id="spacetimeGrid" stroke="#4895ef" stroke-width="1" opacity="0.6">
      <!-- Horizontal lines with wave animation -->
      <path d="M 100 -60 Q 200 -70, 300 -60 T 500 -70 T 700 -60" fill="none">
        <animate attributeName="d" 
                 values="M 100 -60 Q 200 -70, 300 -60 T 500 -70 T 700 -60;
                         M 100 -60 Q 200 -50, 300 -60 T 500 -50 T 700 -60;
                         M 100 -60 Q 200 -70, 300 -60 T 500 -70 T 700 -60" 
                 dur="8s" repeatCount="indefinite" />
      </path>
      
      <path d="M 100 -40 Q 200 -50, 300 -40 T 500 -50 T 700 -40" fill="none">
        <animate attributeName="d" 
                 values="M 100 -40 Q 200 -50, 300 -40 T 500 -50 T 700 -40;
                         M 100 -40 Q 200 -30, 300 -40 T 500 -30 T 700 -40;
                         M 100 -40 Q 200 -50, 300 -40 T 500 -50 T 700 -40" 
                 dur="8s" repeatCount="indefinite" />
      </path>
      
      <path d="M 100 -20 Q 200 -30, 300 -20 T 500 -30 T 700 -20" fill="none">
        <animate attributeName="d" 
                 values="M 100 -20 Q 200 -30, 300 -20 T 500 -30 T 700 -20;
                         M 100 -20 Q 200 -10, 300 -20 T 500 -10 T 700 -20;
                         M 100 -20 Q 200 -30, 300 -20 T 500 -30 T 700 -20" 
                 dur="8s" repeatCount="indefinite" />
      </path>
      
      <!-- Vertical lines with wave animation -->
      <path d="M 150 -70 Q 160 -40, 150 -10" fill="none">
        <animate attributeName="d" 
                 values="M 150 -70 Q 160 -40, 150 -10;
                         M 150 -70 Q 140 -40, 150 -10;
                         M 150 -70 Q 160 -40, 150 -10" 
                 dur="7s" repeatCount="indefinite" />
      </path>
      
      <path d="M 300 -70 Q 310 -40, 300 -10" fill="none">
        <animate attributeName="d" 
                 values="M 300 -70 Q 310 -40, 300 -10;
                         M 300 -70 Q 290 -40, 300 -10;
                         M 300 -70 Q 310 -40, 300 -10" 
                 dur="7s" repeatCount="indefinite" />
      </path>
      
      <path d="M 450 -70 Q 460 -40, 450 -10" fill="none">
        <animate attributeName="d" 
                 values="M 450 -70 Q 460 -40, 450 -10;
                         M 450 -70 Q 440 -40, 450 -10;
                         M 450 -70 Q 460 -40, 450 -10" 
                 dur="7s" repeatCount="indefinite" />
      </path>
      
      <path d="M 600 -70 Q 610 -40, 600 -10" fill="none">
        <animate attributeName="d" 
                 values="M 600 -70 Q 610 -40, 600 -10;
                         M 600 -70 Q 590 -40, 600 -10;
                         M 600 -70 Q 610 -40, 600 -10" 
                 dur="7s" repeatCount="indefinite" />
      </path>
    </g>
    
    <!-- Energy particles flowing through spacetime -->
    <g id="energyParticles">
      <circle cx="150" cy="-40" r="3" fill="white" opacity="0.8">
        <animate attributeName="cx" from="100" to="700" dur="6s" begin="0s" repeatCount="indefinite" />
        <animate attributeName="cy" values="-40; -50; -40; -30; -40" dur="6s" begin="0s" repeatCount="indefinite" />
      </circle>
      <circle cx="150" cy="-40" r="3" fill="white" opacity="0.8">
        <animate attributeName="cx" from="100" to="700" dur="6s" begin="2s" repeatCount="indefinite" />
        <animate attributeName="cy" values="-40; -30; -40; -50; -40" dur="6s" begin="2s" repeatCount="indefinite" />
      </circle>
      <circle cx="150" cy="-40" r="3" fill="white" opacity="0.8">
        <animate attributeName="cx" from="100" to="700" dur="6s" begin="4s" repeatCount="indefinite" />
        <animate attributeName="cy" values="-30; -40; -50; -40; -30" dur="6s" begin="4s" repeatCount="indefinite" />
      </circle>
    </g>
    
    <!-- Spacetime formula -->
    <text x="100" y="-10" font-family="Arial, sans-serif" font-size="12" fill="#8ecae6" text-anchor="start">
      d(A, B) = α·ℓ<tspan baseline-shift="sub" font-size="8">p</tspan>/ln[S<tspan baseline-shift="sub" font-size="8">max</tspan>/S<tspan baseline-shift="sub" font-size="8">ent</tspan>(A:B)]
    </text>
  </g>
  
  <!-- Macroscopic Phenomena Layer (Top) -->
  <g id="macroLayer" transform="translate(0, 100)">
    <rect x="50" y="-80" width="700" height="100" rx="10" fill="url(#macroGradient)" opacity="0.2" />
    <text x="400" y="-55" font-family="Arial, sans-serif" font-size="16" fill="white" text-anchor="middle">Macroscopic Cosmic Phenomena</text>
    
    <!-- Cosmic horizon -->
    <ellipse cx="400" cy="-20" rx="300" ry="30" stroke="#f72585" stroke-width="2" fill="none" opacity="0.6">
      <animate attributeName="rx" values="300;310;300" dur="10s" repeatCount="indefinite" />
      <animate attributeName="ry" values="30;35;30" dur="10s" repeatCount="indefinite" />
    </ellipse>
    
    <!-- Universe expansion animation -->
    <g id="universeBodies">
      <!-- Galaxies moving away from center -->
      <g id="galaxy1" transform="translate(300, -20)">
        <circle r="5" fill="#f1faee" />
        <circle r="8" fill="none" stroke="#f1faee" stroke-width="1" opacity="0.3" />
        <animateTransform attributeName="transform" type="translate" from="350, -20" to="250, -20" dur="20s" repeatCount="indefinite" />
      </g>
      
      <g id="galaxy2" transform="translate(500, -20)">
        <circle r="5" fill="#f1faee" />
        <circle r="8" fill="none" stroke="#f1faee" stroke-width="1" opacity="0.3" />
        <animateTransform attributeName="transform" type="translate" from="450, -20" to="550, -20" dur="20s" repeatCount="indefinite" />
      </g>
      
      <g id="galaxy3" transform="translate(400, 0)">
        <circle r="5" fill="#f1faee" />
        <circle r="8" fill="none" stroke="#f1faee" stroke-width="1" opacity="0.3" />
        <animateTransform attributeName="transform" type="translate" from="400, -10" to="400, 10" dur="20s" repeatCount="indefinite" />
      </g>
      
      <g id="galaxy4" transform="translate(400, -40)">
        <circle r="5" fill="#f1faee" />
        <circle r="8" fill="none" stroke="#f1faee" stroke-width="1" opacity="0.3" />
        <animateTransform attributeName="transform" type="translate" from="400, -30" to="400, -50" dur="20s" repeatCount="indefinite" />
      </g>
    </g>
    
    <!-- Cosmic-scale entropy formula -->
    <text x="100" y="-10" font-family="Arial, sans-serif" font-size="12" fill="#8ecae6" text-anchor="start">
      Λ<tspan baseline-shift="sub" font-size="8">eff</tspan> = (ℏG/c<tspan baseline-shift="super" font-size="8">5</tspan>)∫f(L)·(1/S<tspan baseline-shift="sub" font-size="8">0</tspan>)·dS(L)/dt·dL
    </text>
  </g>
  
  <!-- Connecting flow animations between layers -->
  <g id="connections">
    <!-- Quantum to Spacetime connections -->
    <path d="M 150 420 C 150 400, 150 380, 150 360" fill="none" stroke="white" stroke-width="1" opacity="0.4" stroke-dasharray="5,5">
      <animate attributeName="stroke-dashoffset" from="0" to="20" dur="2s" repeatCount="indefinite" />
    </path>
    <path d="M 300 420 C 300 400, 300 380, 300 360" fill="none" stroke="white" stroke-width="1" opacity="0.4" stroke-dasharray="5,5">
      <animate attributeName="stroke-dashoffset" from="0" to="20" dur="2s" repeatCount="indefinite" />
    </path>
    <path d="M 450 420 C 450 400, 450 380, 450 360" fill="none" stroke="white" stroke-width="1" opacity="0.4" stroke-dasharray="5,5">
      <animate attributeName="stroke-dashoffset" from="0" to="20" dur="2s" repeatCount="indefinite" />
    </path>
    <path d="M 600 420 C 600 400, 600 380, 600 360" fill="none" stroke="white" stroke-width="1" opacity="0.4" stroke-dasharray="5,5">
      <animate attributeName="stroke-dashoffset" from="0" to="20" dur="2s" repeatCount="indefinite" />
    </path>
    
    <!-- Spacetime to Macro connections -->
    <path d="M 150 220 C 150 200, 150 180, 150 160" fill="none" stroke="white" stroke-width="1" opacity="0.4" stroke-dasharray="5,5">
      <animate attributeName="stroke-dashoffset" from="0" to="20" dur="2s" repeatCount="indefinite" />
    </path>
    <path d="M 300 220 C 300 200, 300 180, 300 160" fill="none" stroke="white" stroke-width="1" opacity="0.4" stroke-dasharray="5,5">
      <animate attributeName="stroke-dashoffset" from="0" to="20" dur="2s" repeatCount="indefinite" />
    </path>
    <path d="M 450 220 C 450 200, 450 180, 450 160" fill="none" stroke="white" stroke-width="1" opacity="0.4" stroke-dasharray="5,5">
      <animate attributeName="stroke-dashoffset" from="0" to="20" dur="2s" repeatCount="indefinite" />
    </path>
    <path d="M 600 220 C 600 200, 600 180, 600 160" fill="none" stroke="white" stroke-width="1" opacity="0.4" stroke-dasharray="5,5">
      <animate attributeName="stroke-dashoffset" from="0" to="20" dur="2s" repeatCount="indefinite" />
    </path>
    
    <!-- Side labels for concept flow -->
    <text x="40" y="390" font-family="Arial, sans-serif" font-size="12" fill="white" text-anchor="middle" transform="rotate(-90, 40, 390)">Emergence</text>
    <text x="760" y="390" font-family="Arial, sans-serif" font-size="12" fill="white" text-anchor="middle" transform="rotate(90, 760, 390)">Scale-Invariant Coupling</text>
    <text x="40" y="190" font-family="Arial, sans-serif" font-size="12" fill="white" text-anchor="middle" transform="rotate(-90, 40, 190)">Entropy Production</text>
    <text x="760" y="190" font-family="Arial, sans-serif" font-size="12" fill="white" text-anchor="middle" transform="rotate(90, 760, 190)">Cosmic Expansion</text>
  </g>
  
  <!-- Key phenomena callouts -->
  <g id="callouts">
    <!-- Arrow of Time -->
    <line x1="140" y1="270" x2="100" y2="240" stroke="#dddfff" stroke-width="1" marker-end="url(#arrowMarker)" />
    <text x="140" y="280" font-family="Arial, sans-serif" font-size="11" fill="#dddfff" text-anchor="start">Arrow of Time</text>
    
    <!-- Dark Energy -->
    <line x1="660" y1="120" x2="700" y2="90" stroke="#dddfff" stroke-width="1" marker-end="url(#arrowMarker)" />
    <text x="660" y="130" font-family="Arial, sans-serif" font-size="11" fill="#dddfff" text-anchor="end">Dark Energy</text>
    
    <!-- Black Hole Formation -->
    <line x1="530" y1="220" x2="560" y2="190" stroke="#dddfff" stroke-width="1" marker-end="url(#arrowMarker)" />
    <text x="530" y="230" font-family="Arial, sans-serif" font-size="11" fill="#dddfff" text-anchor="middle">Black Hole Formation</text>
  </g>
  
  <!-- Legend -->
  <g id="legend" transform="translate(400, 530)">
    <rect x="-175" y="0" width="350" height="50" rx="5" fill="#050A30" stroke="white" stroke-width="1" opacity="0.7" />
    
    <circle cx="-150" cy="15" r="5" fill="url(#quantumGradient)" />
    <text x="-135" y="18" font-family="Arial, sans-serif" font-size="10" fill="white" text-anchor="start">Quantum Information</text>
    
    <circle cx="-20" cy="15" r="5" fill="url(#spacetimeGradient)" />
    <text x="-5" y="18" font-family="Arial, sans-serif" font-size="10" fill="white" text-anchor="start">Emergent Spacetime</text>
    
    <circle cx="110" cy="15" r="5" fill="url(#macroGradient)" />
    <text x="125" y="18" font-family="Arial, sans-serif" font-size="10" fill="white" text-anchor="start">Cosmic Phenomena</text>
    
    <line x1="-150" y1="35" x2="-130" y2="35" stroke="white" stroke-width="1" stroke-dasharray="5,5" />
    <text x="-125" y="38" font-family="Arial, sans-serif" font-size="10" fill="white" text-anchor="start">Information Flow</text>
    
    <circle cx="20" cy="35" r="3" fill="white">
      <animate attributeName="r" from="2" to="4" dur="2s" repeatCount="indefinite" />
    </circle>
    <text x="30" y="38" font-family="Arial, sans-serif" font-size="10" fill="white" text-anchor="start">Entropy Production</text>
  </g>
  
  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrowMarker" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#dddfff" />
    </marker>
  </defs>
  
  <!-- Additional Decorative Elements -->
  <g id="decorations">
    <!-- Quantum fluctuations in background -->
    <g id="quantumDots" opacity="0.2">
      <circle cx="50" cy="100" r="1" fill="white">
        <animate attributeName="opacity" values="0.1;0.5;0.1" dur="3s" repeatCount="indefinite" />
      </circle>
      <circle cx="750" cy="500" r="1" fill="white">
        <animate attributeName="opacity" values="0.1;0.5;0.1" dur="4s" repeatCount="indefinite" />
      </circle>
      <circle cx="200" cy="550" r="1" fill="white">
        <animate attributeName="opacity" values="0.1;0.5;0.1" dur="5s" repeatCount="indefinite" />
      </circle>
      <circle cx="650" cy="150" r="1" fill="white">
        <animate attributeName="opacity" values="0.1;0.5;0.1" dur="4.5s" repeatCount="indefinite" />
      </circle>
      <circle cx="400" cy="300" r="1" fill="white">
        <animate attributeName="opacity" values="0.1;0.5;0.1" dur="3.5s" repeatCount="indefinite" />
      </circle>
      <!-- Add more random dots as needed -->
    </g>
  </g>
</svg>