<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aluraflix</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #e50914;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        h1 {
            margin: 0;
            font-size: 2.5em;
        }
        main {
            padding: 20px;
        }
        h2 {
            color: #e50914;
            margin-top: 30px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background-color: #333;
            margin: 10px 0;
            padding: 15px;
            border-radius: 4px;
            font-size: 1.2em;
        }
        .video-container {
            text-align: center;
            margin-top: 30px;
        }
        .video-container iframe {
            width: 100%;
            max-width: 720px;
            height: 405px;
            border: none;
            border-radius: 8px;
        }
    </style>
</head>
<body>

    <header>
        <h1>Aluraflix</h1>
    </header>

    <main>
        <h2>Lista de Filmes</h2>
        <ul>
            <li>O Exorcismo</li>
            <li>Um dia de Cão</li>
            <li>Superman</li>
            <li>Beetle Juice</li>
            <li>Batman</li>
            <li>Matrix</li>
            <li>Happy Feet</li>
            <li>O Curioso Caso de Benjamin Button</li>
            <li>A Origem</li>
            <li>Trilogia de O Senhor dos Anéis</li>
        </ul>

        <div class="video-container">
            <h2>Recomendação dos Filmes</h2>
            <iframe src="https://www.youtube.com/embed/FzgbcFy7GTY" allowfullscreen></iframe>
        </div>
    </main>

</body>
</html>