function validateForm(form) {
  var name = document.getElementById("name").value;
  var username = document.getElementById("user").value;
  var password = document.getElementById("pass").value;
  var repeatPassword = document.getElementById("repass").value;
  var email = document.getElementById("email").value;
  var telephone = document.getElementById("tel").value;
  var genderElements = document.getElementsByName("gender");
  
  var validEmail = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  var containsDigit = /\d/;

  var invalid = [];

  if (name.trim() === "") {
    invalid.push({ field: "name", message: "Name cannot be blank" });
  }

  if (username.trim() === "") {
    invalid.push({ field: "username", message: "Username cannot be blank" });
  }

  if (password.trim() === "") {
    invalid.push({ field: "password", message: "Password cannot be blank" });
  }

  if (repeatPassword.trim() === "") {
    invalid.push({ field: "repass", message: "Repeat Password cannot be blank" });
  }

  if (email.trim() === "") {
    invalid.push({ field: "email", message: "Email cannot be blank" });
  }

  if (telephone.trim() === "") {
    invalid.push({ field: "tel", message: "Telephone cannot be blank" });
  }

  if (password !== repeatPassword) {
    invalid.push({ field: "repass", message: "Passwords do not match" });
  }

  var selectedGender = Array.from(genderElements).some((gender) => gender.checked);
  if (!selectedGender) {
    invalid.push({ field: "gender", message: "Please select a gender" });
  }

  if (!validEmail.test(email)) {
    invalid.push({ field: "email", message: "Invalid email format" });
  }

  if (!/^\+?\d+$/.test(telephone)) {
    invalid.push({ field: "tel", message: "Telephone should contain only digits and may start with +" });
  }

  console.log(invalid);

  var errorsList = document.getElementById("errors");

  errorsList.innerHTML = "";
  clearErrorIndicators();

  if (invalid.length !== 0) {
    invalid.forEach(function (error) {
      var li = document.createElement("li");
      li.textContent = error.message;
      errorsList.appendChild(li);

      document.getElementById(error.field).classList.add("error");
    });

    return false;
  }

  return true;
}

function clearErrorIndicators() {
  var formFields = document.querySelectorAll(".form-field");
  formFields.forEach(function (field) {
    field.classList.remove("error");
  });
}
