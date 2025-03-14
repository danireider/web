import os

# Estructura de carpetas y archivos
structure = {
    "Basics": {
        "CSS_HOME": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS HOME</title><link rel="stylesheet" href="styles.css"></head><body><div class="welcome">¡Aprende CSS con nosotros!</div></body></html>',
            "styles.css": '.welcome { text-align: center; padding: 25px; background-color: #e0f7fa; }'
        },
        "CSS_Introduction": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Introduction</title><link rel="stylesheet" href="styles.css"></head><body><p>¡Haz que destaque!</p></body></html>',
            "styles.css": 'p { color: purple; font-size: 18px; }'
        },
        "CSS_Syntax": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Syntax</title><link rel="stylesheet" href="styles.css"></head><body><h2>Hola Mundo</h2></body></html>',
            "styles.css": 'h2 { text-align: right; color: orange; }'
        },
        "CSS_Selectors": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Selectors</title><link rel="stylesheet" href="styles.css"></head><body><p class="note" id="first">Esto es una nota.</p></body></html>',
            "styles.css": 'p { color: gray; } .note { font-style: italic; } #first { border: 1px solid; }'
        },
        "CSS_How_To": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS How To</title><style>p { color: navy; }</style><link rel="stylesheet" href="mystyle.css"></head><body><p style="color: teal;">Estilo inline</p></body></html>',
            "styles.css": '/* mystyle.css */ p { color: coral; }'
        },
        "CSS_Comments": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Comments</title><link rel="stylesheet" href="styles.css"></head><body><p>Texto en negrita</p></body></html>',
            "styles.css": '/* Esto hace el texto en negrita */ p { font-weight: bold; }'
        }
    },
    "Colors_and_Backgrounds": {
        "CSS_Colors": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Colors</title><link rel="stylesheet" href="styles.css"></head><body><div class="box">Caja colorida</div></body></html>',
            "styles.css": '.box { color: rgb(0, 150, 0); }'
        },
        "CSS_Backgrounds": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Backgrounds</title><link rel="stylesheet" href="styles.css"></head><body><div class="bg">Fondo bonito</div></body></html>',
            "styles.css": '.bg { background: #f5f5f5 url("pattern.png") repeat top left; height: 100px; }'
        },
        "CSS_Borders": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Borders</title><link rel="stylesheet" href="styles.css"></head><body><div class="edge">Caja con bordes</div></body></html>',
            "styles.css": '.edge { border: 3px dotted red; padding: 10px; }'
        },
        "CSS_Margins": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Margins</title><link rel="stylesheet" href="styles.css"></head><body><div class="space">Espaciado</div></body></html>',
            "styles.css": '.space { margin: 20px; background-color: #ffebee; }'
        },
        "CSS_Padding": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Padding</title><link rel="stylesheet" href="styles.css"></head><body><div class="inner">Relleno interno</div></body></html>',
            "styles.css": '.inner { padding: 15px; border: 1px solid black; }'
        },
        "CSS_Height_Width": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Height/Width</title><link rel="stylesheet" href="styles.css"></head><body><div class="size">Caja dimensionada</div></body></html>',
            "styles.css": '.size { width: 150px; height: 80px; background-color: #c8e6c9; }'
        },
        "CSS_Box_Model": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Box Model</title><link rel="stylesheet" href="styles.css"></head><body><div class="box-model">Caja</div></body></html>',
            "styles.css": '.box-model { width: 100px; padding: 10px; border: 2px solid blue; margin: 15px; }'
        },
        "CSS_Outline": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Outline</title><link rel="stylesheet" href="styles.css"></head><body><div class="outline">Contorneado</div></body></html>',
            "styles.css": '.outline { outline: 2px dashed purple; padding: 5px; }'
        }
    },
    "Text_and_Fonts": {
        "CSS_Text": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Text</title><link rel="stylesheet" href="styles.css"></head><body><p class="text">Texto elegante</p></body></html>',
            "styles.css": '.text { text-align: center; text-decoration: overline; }'
        },
        "CSS_Fonts": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Fonts</title><link rel="stylesheet" href="styles.css"></head><body><p class="font">Fuente estilizada</p></body></html>',
            "styles.css": '.font { font-family: Georgia, serif; font-size: 22px; }'
        },
        "CSS_Icons": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Icons</title><link rel="stylesheet" href="styles.css"></head><body><span class="icon">★</span></body></html>',
            "styles.css": '.icon { font-size: 30px; color: gold; }'
        },
        "CSS_Links": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Links</title><link rel="stylesheet" href="styles.css"></head><body><a href="#">Haz clic aquí</a></body></html>',
            "styles.css": 'a:link { color: blue; } a:hover { color: pink; }'
        },
        "CSS_Lists": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Lists</title><link rel="stylesheet" href="styles.css"></head><body><ul class="list"><li>Item 1</li><li>Item 2</li></ul></body></html>',
            "styles.css": '.list { list-style-type: square; }'
        },
        "CSS_Tables": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Tables</title><link rel="stylesheet" href="styles.css"></head><body><table class="table"><tr><td>Celda</td></tr></table></body></html>',
            "styles.css": '.table { border-collapse: collapse; } td { border: 1px solid gray; }'
        }
    },
    "Layout_and_Positioning": {
        "CSS_Display": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Display</title><link rel="stylesheet" href="styles.css"></head><body><span class="block">Span en bloque</span></body></html>',
            "styles.css": '.block { display: block; background-color: #fff9c4; }'
        },
        "CSS_Max_width": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Max-width</title><link rel="stylesheet" href="styles.css"></head><body><div class="max">Ancho limitado</div></body></html>',
            "styles.css": '.max { max-width: 200px; background-color: #b2ebf2; }'
        },
        "CSS_Position": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Position</title><link rel="stylesheet" href="styles.css"></head><body><div class="pos">Movido</div></body></html>',
            "styles.css": '.pos { position: absolute; top: 20px; left: 30px; }'
        },
        "CSS_Z_index": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Z-index</title><link rel="stylesheet" href="styles.css"></head><body><div class="layer1">Capa 1</div><div class="layer2">Capa 2</div></body></html>',
            "styles.css": '.layer1 { position: absolute; z-index: 1; background: #ccc; } .layer2 { position: absolute; z-index: 2; background: #999; }'
        },
        "CSS_Overflow": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Overflow</title><link rel="stylesheet" href="styles.css"></head><body><div class="overflow">Texto largo aquí...</div></body></html>',
            "styles.css": '.overflow { width: 100px; height: 50px; overflow: scroll; }'
        },
        "CSS_Float": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Float</title><link rel="stylesheet" href="styles.css"></head><body><img class="float" src="image.jpg"><p>El texto se envuelve.</p></body></html>',
            "styles.css": '.float { float: right; width: 50px; }'
        },
        "CSS_Inline_block": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Inline-block</title><link rel="stylesheet" href="styles.css"></head><body><div class="inline">Uno</div><div class="inline">Dos</div></body></html>',
            "styles.css": '.inline { display: inline-block; width: 60px; background-color: #dcedc8; }'
        },
        "CSS_Align": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Align</title><link rel="stylesheet" href="styles.css"></head><body><div class="align">Centrado</div></body></html>',
            "styles.css": '.align { text-align: center; }'
        },
        "CSS_Combinators": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Combinators</title><link rel="stylesheet" href="styles.css"></head><body><div><span>Dentro del div</span></div></body></html>',
            "styles.css": 'div span { color: teal; }'
        },
        "CSS_Pseudo_class": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Pseudo-class</title><link rel="stylesheet" href="styles.css"></head><body><button class="btn">Pasa el mouse</button></body></html>',
            "styles.css": '.btn:hover { background-color: #ffccbc; }'
        },
        "CSS_Pseudo_element": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Pseudo-element</title><link rel="stylesheet" href="styles.css"></head><body><p class="extra">Texto</p></body></html>',
            "styles.css": '.extra::before { content: ">> "; color: red; }'
        },
        "CSS_Opacity": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Opacity</title><link rel="stylesheet" href="styles.css"></head><body><div class="fade">Desvanecido</div></body></html>',
            "styles.css": '.fade { opacity: 0.7; background-color: #b3e5fc; }'
        },
        "CSS_Navigation_Bar": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Navigation Bar</title><link rel="stylesheet" href="styles.css"></head><body><ul class="nav"><li><a href="#">Inicio</a></li><li><a href="#">Acerca de</a></li></ul></body></html>',
            "styles.css": '.nav { list-style-type: none; background-color: #424242; } .nav li { display: inline; } .nav a { color: white; padding: 10px; }'
        },
        "CSS_Dropdowns": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Dropdowns</title><link rel="stylesheet" href="styles.css"></head><body><div class="dropdown">Menú<div class="content">Opción 1</div></div></body></html>',
            "styles.css": '.dropdown:hover .content { display: block; } .content { display: none; background-color: #f5f5f5; }'
        },
        "CSS_Image_Gallery": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Image Gallery</title><link rel="stylesheet" href="styles.css"></head><body><div class="gallery"><img src="img1.jpg"><img src="img2.jpg"></div></body></html>',
            "styles.css": '.gallery img { width: 100px; margin: 5px; }'
        },
        "CSS_Image_Sprites": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Image Sprites</title><link rel="stylesheet" href="styles.css"></head><body><div class="sprite"></div></body></html>',
            "styles.css": '.sprite { width: 50px; height: 50px; background: url("sprites.png") 0 0; }'
        },
        "CSS_Attr_Selectors": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Attr Selectors</title><link rel="stylesheet" href="styles.css"></head><body><input type="email"></body></html>',
            "styles.css": '[type="email"] { border: 2px solid green; }'
        },
        "CSS_Forms": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Forms</title><link rel="stylesheet" href="styles.css"></head><body><input class="form-input" type="text"></body></html>',
            "styles.css": '.form-input { padding: 8px; border-radius: 4px; }'
        },
        "CSS_Counters": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Counters</title><link rel="stylesheet" href="styles.css"></head><body><ol class="count"><li>Uno</li><li>Dos</li></ol></body></html>',
            "styles.css": '.count { counter-reset: mycount; } .count li::before { counter-increment: mycount; content: counter(mycount) ". "; }'
        },
        "CSS_Website_Layout": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Website Layout</title><link rel="stylesheet" href="styles.css"></head><body><div class="layout"><header>Encabezado</header><main>Principal</main></div></body></html>',
            "styles.css": 'header { background: #b0bec5; } main { background: #eceff1; }'
        },
        "CSS_Units": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Units</title><link rel="stylesheet" href="styles.css"></head><body><div class="unit">Dimensionado</div></body></html>',
            "styles.css": '.unit { width: 50%; padding: 1em; }'
        },
        "CSS_Specificity": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Specificity</title><link rel="stylesheet" href="styles.css"></head><body><div class="spec" id="unique">Texto</div></body></html>',
            "styles.css": 'div { color: blue; } .spec { color: green; } #unique { color: red; }'
        },
        "CSS_Important": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS !important</title><link rel="stylesheet" href="styles.css"></head><body><p class="force">Color forzado</p></body></html>',
            "styles.css": 'p { color: blue; } .force { color: gray !important; }'
        },
        "CSS_Math_Functions": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Math Functions</title><link rel="stylesheet" href="styles.css"></head><body><div class="calc">Calculado</div></body></html>',
            "styles.css": '.calc { width: calc(100% - 40px); background: #fff3e0; }'
        }
    },
    "Advanced": {
        "CSS_Rounded_Corners": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Rounded Corners</title><link rel="stylesheet" href="styles.css"></head><body><div class="round">Redondeado</div></body></html>',
            "styles.css": '.round { border-radius: 20px; background: #e8f5e9; }'
        },
        "CSS_Border_Images": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Border Images</title><link rel="stylesheet" href="styles.css"></head><body><div class="border-img">Borde elegante</div></body></html>',
            "styles.css": '.border-img { border: 10px solid; border-image: url("frame.png") 10 stretch; }'
        },
        "CSS_Backgrounds_Advanced": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Backgrounds (Advanced)</title><link rel="stylesheet" href="styles.css"></head><body><div class="multi-bg">Capas</div></body></html>',
            "styles.css": '.multi-bg { background: url("top.png"), #ddd; height: 120px; }'
        },
        "CSS_Colors_Advanced": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Colors (Advanced)</title><link rel="stylesheet" href="styles.css"></head><body><div class="adv-color">Color profundo</div></body></html>',
            "styles.css": '.adv-color { color: hsl(200, 50%, 60%); }'
        },
        "CSS_Color_Keywords": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Color Keywords</title><link rel="stylesheet" href="styles.css"></head><body><div class="keyword">Transparente</div></body></html>',
            "styles.css": '.keyword { background-color: transparent; border: 1px solid; }'
        },
        "CSS_Gradients": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Gradients</title><link rel="stylesheet" href="styles.css"></head><body><div class="grad">Gradiente</div></body></html>',
            "styles.css": '.grad { background: linear-gradient(to right, #ffeb3b, #4caf50); height: 80px; }'
        },
        "CSS_Shadows": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Shadows</title><link rel="stylesheet" href="styles.css"></head><body><div class="shadow">Sombreado</div></body></html>',
            "styles.css": '.shadow { box-shadow: 3px 3px 6px #888; }'
        },
        "CSS_Text_Effects": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Text Effects</title><link rel="stylesheet" href="styles.css"></head><body><p class="effect">Brillante</p></body></html>',
            "styles.css": '.effect { text-shadow: 1px 1px 2px pink; }'
        },
        "CSS_Web_Fonts": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Web Fonts</title><link rel="stylesheet" href="styles.css"></head><body><p class="web-font">Fuente personalizada</p></body></html>',
            "styles.css": '@font-face { font-family: "MyFont"; src: url("myfont.woff"); } .web-font { font-family: "MyFont", sans-serif; }'
        },
        "CSS_2D_Transforms": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS 2D Transforms</title><link rel="stylesheet" href="styles.css"></head><body><div class="transform">Inclinado</div></body></html>',
            "styles.css": '.transform { transform: rotate(15deg); background: #f3e5f5; }'
        },
        "CSS_3D_Transforms": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS 3D Transforms</title><link rel="stylesheet" href="styles.css"></head><body><div class="transform-3d">3D</div></body></html>',
            "styles.css": '.transform-3d { transform: perspective(300px) rotateY(30deg); }'
        },
        "CSS_Transitions": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Transitions</title><link rel="stylesheet" href="styles.css"></head><body><div class="trans">Pasa el mouse</div></body></html>',
            "styles.css": '.trans { width: 100px; transition: width 0.4s; } .trans:hover { width: 150px; }'
        },
        "CSS_Animations": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Animations</title><link rel="stylesheet" href="styles.css"></head><body><div class="anim">Moviendo</div></body></html>',
            "styles.css": '@keyframes slide { from { margin-left: 0; } to { margin-left: 50px; } } .anim { animation: slide 2s infinite; }'
        },
        "CSS_Tooltips": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Tooltips</title><link rel="stylesheet" href="styles.css"></head><body><div class="tooltip">Pasa el mouse<span class="tip">¡Hola!</span></div></body></html>',
            "styles.css": '.tip { display: none; position: absolute; background: #eee; } .tooltip:hover .tip { display: block; }'
        },
        "CSS_Style_Images": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Style Images</title><link rel="stylesheet" href="styles.css"></head><body><img class="styled" src="pic.jpg"></body></html>',
            "styles.css": '.styled { filter: grayscale(50%); }'
        },
        "CSS_Image_Reflection": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Image Reflection</title><link rel="stylesheet" href="styles.css"></head><body><img class="reflect" src="pic.jpg"></body></html>',
            "styles.css": '.reflect { -webkit-box-reflect: below 0px; }'
        },
        "CSS_object_fit": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS object-fit</title><link rel="stylesheet" href="styles.css"></head><body><img class="fit" src="pic.jpg"></body></html>',
            "styles.css": '.fit { width: 100px; height: 100px; object-fit: cover; }'
        },
        "CSS_object_position": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS object-position</title><link rel="stylesheet" href="styles.css"></head><body><img class="pos-img" src="pic.jpg"></body></html>',
            "styles.css": '.pos-img { object-position: 20% 80%; }'
        },
        "CSS_Masking": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Masking</title><link rel="stylesheet" href="styles.css"></head><body><div class="mask">Enmascarado</div></body></html>',
            "styles.css": '.mask { mask-image: url("mask.png"); background: #ffcc80; }'
        },
        "CSS_Buttons": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Buttons</title><link rel="stylesheet" href="styles.css"></head><body><button class="btn-style">Haz clic</button></body></html>',
            "styles.css": '.btn-style { padding: 10px 20px; background: #4db6ac; border: none; }'
        },
        "CSS_Pagination": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Pagination</title><link rel="stylesheet" href="styles.css"></head><body><div class="pages"><a href="#">1</a><a href="#">2</a></div></body></html>',
            "styles.css": '.pages a { padding: 8px; background: #e0e0e0; }'
        },
        "CSS_Multiple_Columns": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Multiple Columns</title><link rel="stylesheet" href="styles.css"></head><body><div class="cols">Mucho texto aquí...</div></body></html>',
            "styles.css": '.cols { column-count: 2; }'
        },
        "CSS_User_Interface": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS User Interface</title><link rel="stylesheet" href="styles.css"></head><body><div class="ui">Redimensionable</div></body></html>',
            "styles.css": '.ui { resize: horizontal; overflow: auto; }'
        },
        "CSS_Variables": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Variables</title><link rel="stylesheet" href="styles.css"></head><body><div class="var">Color variable</div></body></html>',
            "styles.css": ':root { --my-color: #ab47bc; } .var { background: var(--my-color); }'
        },
        "CSS_Box_Sizing": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Box Sizing</title><link rel="stylesheet" href="styles.css"></head><body><div class="box-size">Caja</div></body></html>',
            "styles.css": '.box-size { box-sizing: border-box; width: 100px; padding: 10px; border: 5px solid; }'
        },
        "CSS_Media_Queries": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Media Queries</title><link rel="stylesheet" href="styles.css"></head><body><div class="mq">Responsive</div></body></html>',
            "styles.css": '.mq { background: #b2dfdb; } @media (max-width: 500px) { .mq { background: #ffecb3; } }'
        },
        "CSS_MQ_Examples": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS MQ Examples</title><link rel="stylesheet" href="styles.css"></head><body><p class="mq-ex">Texto</p></body></html>',
            "styles.css": '@media (min-width: 400px) { .mq-ex { font-size: 20px; } }'
        },
        "CSS_Flexbox": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>CSS Flexbox</title><link rel="stylesheet" href="styles.css"></head><body><div class="flex"><div>1</div><div>2</div></div></body></html>',
            "styles.css": '.flex { display: flex; justify-content: space-between; }'
        }
    },
    "Responsive": {
        "RWD_Intro": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>RWD Intro</title><link rel="stylesheet" href="styles.css"></head><body><div class="rwd">Adaptable</div></body></html>',
            "styles.css": '.rwd { width: 100%; max-width: 600px; }'
        },
        "RWD_Viewport": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>RWD Viewport</title><link rel="stylesheet" href="styles.css"></head><body><div>Contenido</div></body></html>',
            "styles.css": '/* No se necesita CSS adicional */'
        },
        "RWD_Grid_View": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>RWD Grid View</title><link rel="stylesheet" href="styles.css"></head><body><div class="rwd-grid"><div>Col 1</div><div>Col 2</div></div></body></html>',
            "styles.css": '.rwd-grid { display: grid; grid-template-columns: 1fr 1fr; } @media (max-width: 400px) { .rwd-grid { grid-template-columns: 1fr; } }'
        },
        "RWD_Media_Queries": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>RWD Media Queries</title><link rel="stylesheet" href="styles.css"></head><body><div class="rwd-mq">Responsive</div></body></html>',
            "styles.css": '@media (max-width: 600px) { .rwd-mq { font-size: 14px; } }'
        },
        "RWD_Images": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>RWD Images</title><link rel="stylesheet" href="styles.css"></head><body><img class="rwd-img" src="pic.jpg"></body></html>',
            "styles.css": '.rwd-img { max-width: 100%; height: auto; }'
        },
        "RWD_Videos": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>RWD Videos</title><link rel="stylesheet" href="styles.css"></head><body><video class="rwd-video" controls><source src="video.mp4"></video></body></html>',
            "styles.css": '.rwd-video { width: 100%; }'
        },
        "RWD_Templates": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>RWD Templates</title><link rel="stylesheet" href="styles.css"></head><body><div class="rwd-template"><header>Arriba</header><main>Medio</main></div></body></html>',
            "styles.css": '@media (max-width: 500px) { .rwd-template header { font-size: 16px; } }'
        }
    },
    "CSS_Grid": {
        "Grid_Intro": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>Grid Intro</title><link rel="stylesheet" href="styles.css"></head><body><div class="grid-intro"><div>A</div><div>B</div></div></body></html>',
            "styles.css": '.grid-intro { display: grid; }'
        },
        "Grid_Container": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>Grid Container</title><link rel="stylesheet" href="styles.css"></head><body><div class="grid-cont"><div>1</div><div>2</div></div></body></html>',
            "styles.css": '.grid-cont { display: grid; grid-template-columns: 1fr 1fr; }'
        },
        "Grid_Item": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>Grid Item</title><link rel="stylesheet" href="styles.css"></head><body><div class="grid-item"><div class="item">Item</div></div></body></html>',
            "styles.css": '.item { grid-column: 1 / 3; }'
        }
    },
    "CSS_SASS": {
        "SASS_Tutorial": {
            "index.html": '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>SASS Tutorial</title><link rel="stylesheet" href="styles.css"></head><body><div class="box"><p>Texto</p></div></body></html>',
            "styles.css": '.box { background: #e1bee7; } .box p { color: #fff; }'
        }
    }
}

# Crear la carpeta principal
os.makedirs("CSS_Examples", exist_ok=True)

# Crear subcarpetas y archivos
for category, subtopics in structure.items():
    category_path = os.path.join("CSS_Examples", category)
    os.makedirs(category_path, exist_ok=True)
    for subtopic, files in subtopics.items():
        subtopic_path = os.path.join(category_path, subtopic)
        os.makedirs(subtopic_path, exist_ok=True)
        for file_name, content in files.items():
            with open(os.path.join(subtopic_path, file_name), "w") as f:
                f.write(content)

print("Carpetas y archivos creados exitosamente.")