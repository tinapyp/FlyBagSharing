document.getElementById("joinButton").addEventListener("click", function () {
  var email = document.getElementById("emailInput").value;

  // Send a POST request to the Flask endpoint
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/add_email");
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.onload = function () {
    if (xhr.status === 200) {
      alert("Email added successfully!");
    } else {
      alert("Failed to add email. Please try again.");
    }
  };
  xhr.send("email=" + encodeURIComponent(email));
});
