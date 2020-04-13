

function postFormData(url, data) {
    return fetch(url, {
            method: "POST",
            body: data
        })
            .then(response => response.json())
            .catch(error => console.log(error));
}

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

function clearThis(target) {
        target.value= "";
    }

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
                let answerDiv= document.createElement("div");
                dialog.appendChild(answerDiv);
                let userQuery = document.createElement("p");
                userQuery.innerHTML = "Moi :" + response["message"]["raw_message"];
                answerDiv.appendChild(userQuery);
                let waitGrandPa = document.createElement("p");
                waitGrandPa.innerHTML = "Grand pa: Attends je cherche...";
                answerDiv.appendChild(waitGrandPa);
                let waitImage = document.createElement("img");
                waitImage.setAttribute("src","https://media.giphy.com/media/MtMkEwDdYRsXe/giphy.gif");
                waitImage.setAttribute("width","200");
                waitImage.setAttribute("height","200");
                answerDiv.appendChild(waitImage);
                setTimeout(function() {
                    let addByGrandPa = document.createElement("p");
                    addByGrandPa.innerHTML = "Grand pa: Voilà l'adresse que tu cherches " + response["google"]["result"]["adr_address"];
                    answerDiv.appendChild(addByGrandPa);
                    initMap(response["google"]["result"]["geometry"]["location"]["lat"], response["google"]["result"]["geometry"]["location"]["lng"]);
                }, 5000);

            })

    }
})











