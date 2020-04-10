const formDivButton = document.getElementById('submit');
formDivButton.addEventListener('click', function(event){
    event.preventDefault();

    const userQuery = document.getElementById("user_request");
    console.log(userQuery.value)
    if (userQuery.value.length < 10) {
       alert("Tu ne dis pas grand chose...");
    } else {
        const divContainer = document.getElementById("container");
        // Removing the formular from index view
        divContainer.removeChild(document.getElementById("formular"));
        // Inserting the map into the view from index view
        const divMap = document.createElement("div");
        divMap.setAttribute("id","divMap");
        divMap.setAttribute("class", "card");
        const divMapTitle = document.createElement("div");
        divMapTitle.innerHTML = "<h2>Voilà ou ça ce trouve !</h2>";
        divMap.appendChild(divMapTitle);
        const divMapResult = document.createElement("div");
        // Insert return of Google maps API
        divMap.appendChild(divMapResult);
        divContainer.appendChild(divMap);
        // Inserting the story into the view from index view
        const divStory = document.createElement("div");
        divStory.setAttribute("id","divMap");
        divStory.setAttribute("class", "card");
        const divStoryTitle = document.createElement("div");
        divStoryTitle.innerHTML = "<h2>Une petite annecdote</h2>";
        divStory.appendChild(divStoryTitle);
        const divStoryResult = document.createElement("div");
        // Insert return of Google maps API
        divStory.appendChild(divStoryResult);
        divContainer.appendChild(divStory);





    }
});

