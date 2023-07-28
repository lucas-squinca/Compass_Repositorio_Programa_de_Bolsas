# Portfólio Lucas Dias Squinca
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](Projeto_portfolio\LICENSE)
>## Projeto de portfólio do curso de Git e GitHub:
>### Acesse: [https://nicitov.github.io](https://nicitov.github.io)

## Código HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfólio Lucas Dias Squinca</title>
    <!-- Google Fonts-->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,700;0,900;1,300;1,700;1,900&display=swap" rel="stylesheet">
    <!-- Dev Icon Fonts-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.15.1/devicon.min.css">
    <!-- CSS do Projeto-->
    <link rel="stylesheet" href="css/styles.css">

</head>
<body>

    <main id="container">
        <aside id="bio-container">
            <h2>Lucas Dias Squinca</h2>
            <img src="img/perfil.jpg" alt="Lucas Dias Squinca">
            <p>Olá, meu nome é Lucas Dias Squinca e sou <span class="highlight">estudante de Sistemas de Informação na UFMS-CPTL</span></p>
            <p id="welcome-text">Seja bem-vindo</p>
            <ul id="social-container">
                <li><a href="https://twitter.com/lucas_squinca" target="_blank"><ion-icon name="logo-twitter"></ion-icon></a></li>
                <li><a href="https://www.instagram.com/lucassquinca/" target="_blank"><ion-icon name="logo-instagram"></ion-icon></a></li>
                <li><a href="https://www.linkedin.com/in/lucas-squinca-32584425b/" target="_blank"><ion-icon name="logo-linkedIn"></ion-icon></a></li>
            </ul>
            <div id="email-container">
                <ion-icon name="mail-outline"></ion-icon><a href="mailto:lucassquinca35@gmail.com">lucassquinca35@gmail.com</a>
            </div>
        </aside>
        <section id="about-container">
            <h1 id="name">Lucas Dias Squinca</h1>
            <p id="title"><span class="highlight">Estudante de S.I na UFMS-CPTL</span></p>
            <p id="description">Sou estudante da área de T.I, cursando meu 2º Semestre em S.I; gosto de <span class="highlight">desenvolver sistemas</span> e sou entusiasta em <span class="highlight">Big Data</span></p>
            <p id="description">Atuo majoritariamente no back-end com <span class="highlight">Linguagens C e Python</span>, mas de vez em quando desenvolvo projetos front-end</p>
            <a href="https://github.com/Nicitov" id="btn-project"><ion-icon name="share-social-outline"></ion-icon> <span>Ver Projetos</span></a>
            <h2 id="skills-section-tittle">Meus Conhecimentos</h2>
            <p id="description">Conheça as tecnologias que domino:</p>
            <div id="skills-container">
                <div id="skills-box">
                    <p class="skills-title">Front-End</p>
                    <i class="devicon-html5-plain colored"></i>
                    <i class="devicon-css3-plain colored"></i>
                </div>
                <div id="skills-box">
                    <p class="skills-title">Back-End</p>
                    <i class="devicon-c-plain colored"></i>
                    <i class="devicon-python-plain colored"></i>
                </div>
                <div id="skills-box">
                    <p class="skills-title">DataBases</p>
                    <i class="devicon-mysql-plain colored"></i>
                </div>
                <div id="skills-box">
                    <p class="skills-title">Front Frameworks</p>
                    <i class="devicon-#-plain colored"></i>
                </div>
                <div id="skills-box">
                    <p class="skills-title">Back Frameworks</p>
                    <i class="devicon-#-plain colored"></i>
                </div>
                <div id="skills-box">
                    <p class="skills-title">Tools</p>
                    <i class="devicon-linux-plain colored"></i>
                </div>
            </div>
        </section>
    </main>
    <!-- Ion Icons-->
    <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
</body>
</html>
```

## Código CSS

```css
/* Reset */

* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: "Roboto";
}

/* Variables */

:root {
    --main-color: #54B689;
    --main-text-color: #FFF;
    --border-color: #999;
    --bio-bg-color: #1E2A3A;
    --bio-border-color: #293544;
    --about-bg-color: #111821;
}

/* General */

.highlight {
    color: var(--main-color);
}

/* Containers */

#container {
    display: flex;
    flex-direction: row;
    color: var(--main-text-color);
}

#bio-container {
    flex: 1 1 20%;
    min-height: 100vh;
    background-color: var(--bio-bg-color);
    text-align: center;
    padding: 30px 12px;
    border-right: 5px solid var(--bio-border-color);
}

#about-container {
    flex: 1 1 80%;
    min-height: 100%;
    background-color: var(--about-bg-color);
    padding: 50px;
}

/* Bio Container */

#bio-container img {
    width: 175px;
    height: 175px;
    border-radius: 50%;
    margin-bottom: 25px;
}

#bio-container h2 {
    margin-bottom: 25px;
}

#bio-container p {
    margin-bottom: 20px;
}

#social-container {
    display: flex;
    justify-content: center;
    list-style: none;
    border-bottom: 1px solid var(--border-color);
}

#bio-container #welcome-text {
    font-weight: bold;
}

#social-container li {
    flex: 1 1 0;
    max-width: 60px;
}

#social-container li a {
    color: var(--main-color);
    font-size: 30px;
}

#email-container {
    display: flex;
    justify-content: center;
}

#email-container ion-icon,
#email-container a {
    flex: 1 1 0;
}

#email-container a {
    color: var(--main-text-color);
    text-decoration: none;
    max-width: 225px;
}

#email-container ion-icon {
    color: var(--main-color);
    font-size: 20px;
    margin-right: 5px;
    max-width: 20px;
}

/* About container */

#name {
    font-size: 42px;
    margin-bottom: 15px;
}

#title {
    font-size: 24px;
    margin-bottom: 15px;
    font-weight: bold;
}

.description {
    max-width: 75%;
    margin-bottom: 10px;
}

#btn-project {
    font-weight: bold;
    font-size: 16px;
    color: var(--main-text-color);
    background-color: var(--main-color);
    border: 2px solid var(--main-color);
    border-radius: 5px;
    text-decoration: none;
    transition: .5s;
    margin: 25px 0;
    padding: 12px 10px;
    width: 150px;
    text-align: center;
    display: flex;
}

#btn-project ion-icon,
#btn-project span {
    flex: 1 1 0;
}

#btn-project ion-icon {
    font-size: 20px;
    max-width: 20px;
}

#btn-project:hover {
    background-color: transparent;
}

#skills-section-tittle {
    border-top: 1px solid var(--border-color);
    padding-top: 20px;
    margin-bottom: 20px;
    font-size: 32px;
}

#skills-container {
    display: flex;
    flex-wrap: wrap;
    margin-top: 25px;
}

#skills-box {
    flex: 1 1 33%;
    max-width: 33%;
    margin-bottom: 35px;
}

.skills-title {
    font-size: 24px;
    margin-bottom: 25px;
    font-weight: bold;
    padding-left: 10px;
    border-left: 5px solid var(--main-color);
}

#skills-box i {
    font-size: 45px;
    margin-right: 10px;
}

/* Mobile */

@media(max-width: 450px) {
    #container {
        flex-direction: column;
    }

    #bio-container {
        min-height: auto;
        border-right: none;
        border-bottom: 5px solid var(--bio-border-color);
    }

    #bio-container h2 {
        display: none;
    }

    #bio-container {
        max-width: 60%;
        margin: 10px auto;
    }

    #about-container {
        text-align: center;
        padding: 30px;
    }
    
    #about-container .description {
        margin: 10px auto;
        max-width: 100%;
        line-height: 26px;

    }

    #btn-project {
        margin: 20px auto;
    }

    .skills-box {
        flex: 1 1 100%;
        max-width: 100%;
        margin-bottom: 40px;
        text-align: left;
    }

    .skills-box i {
        font-size: 60px;
    }
}
```