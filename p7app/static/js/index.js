
// Function to intercept answer coming from back end
function postFormData(url, data) {
    return fetch(url, {
            method: "POST",
            body: data
        })
            .then(response => response.json())
            .catch(error => console.log(error));
}

// Function to generate the MAP object to display
function initMap(latitude, longitude) {
        var myLatLng = {lat: latitude, lng: longitude};
        var map = new google.maps.Map(document.getElementById("map"),{
        center: myLatLng,
        zoom: 10
    });
        var marker = new google.maps.Marker({
            position: myLatLng,
            map: map,
            title: 'Hello World!'
        });
}

// function to clear a element on view. IE
function clearThis(target) {
        target.value= "";
    }

// Managing the formular submission
let formular = document.querySelector('#formular');
formular.addEventListener('submit', function(event) {
    event.preventDefault();
    const userQuery = document.getElementById("user_request");
    if (userQuery.value.length < 10) {
        alert("Tu ne dis pas grand chose...");
    } else {
        postFormData("/results", new FormData(formular))
            .then(response => {
                let input = document.getElementById("user_request");
                clearThis(document.getElementById("user_request"));
                let dialog = document.getElementById("dialog");
                let answerDiv = document.createElement("div");
                dialog.appendChild(answerDiv);
                let userQuery = document.createElement("p");
                userQuery.innerHTML = "Moi :" + response["messages"]["raw_message"];
                answerDiv.appendChild(userQuery);
                let waitGrandPa = document.createElement("p");
                waitGrandPa.innerHTML = "Grand pa: Attends je cherche...";
                answerDiv.appendChild(waitGrandPa);
                let waitImage = document.createElement("img");
                waitImage.setAttribute("src", "https://media.giphy.com/media/MtMkEwDdYRsXe/giphy.gif");
                waitImage.setAttribute("width", "200");
                waitImage.setAttribute("height", "200");
                answerDiv.appendChild(waitImage);
                let addByGrandPa = document.createElement("p");
                // Timer to delay the answer
                setTimeout(function () {
                    /// Manage answer if results have been found
                    if (response["status"] === "OK") {
                        addByGrandPa.innerHTML = "Grand pa: Voilà l'adresse que tu cherches " + response["google"]["result"]["adr_address"];
                        initMap(response["google"]["result"]["geometry"]["location"]["lat"], response["google"]["result"]["geometry"]["location"]["lng"]);
                    /// Managing errors and display an answer accordingly
                    } else {

                        /// Request valid but no results found
                        if (response["status"] === 'ZERO_RESULTS') {
                            addByGrandPa.innerHTML = "Grand pa: J'ai bien cherché, mais je n'ai rien retrouvé ";

                         /// Managing parsing error
                        } else if (response["errors"]["parser"] === true){
                            addByGrandPa.innerHTML = "Grand pa: Je n'ai rien compris. Repose ta question ";
                         /// Managing parsing error
                        } else if (response["errors"]["searchAPI"] === true){
                            addByGrandPa.innerHTML = "Grand pa: Je débloque, repose ta question ";
                        } else if (response["errors"]["resultsAPI"] === true){
                            addByGrandPa.innerHTML = "Grand pa: Je suis vieux, je perd la mémoire de temps en temps ";
                        }



                    }

                }, 5000);
                document.getElementById( 'dialog' ).scrollIntoView(false);
                answerDiv.appendChild(addByGrandPa);




    })

    }
})











