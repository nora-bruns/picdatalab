---
layout: page
title: Publications
permalink: /publications/
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PubMed Articles</title>
</head>
<body>
    <h1>Latest PubMed Articles</h1>
    <ul id="articles"></ul>

    <script>
        fetch('pubmed.json')
            .then(response => response.json())
            .then(data => {
                let articles = data.article_ids;
                let list = document.getElementById("articles");

                articles.forEach(id => {
                    let li = document.createElement("li");
                    li.innerHTML = `<a href="https://pubmed.ncbi.nlm.nih.gov/${id}/" target="_blank">PubMed Article ${id}</a>`;
                    list.appendChild(li);
                });
            })
            .catch(error => console.error('Error loading PubMed data:', error));
    </script>
</body>
</html>
