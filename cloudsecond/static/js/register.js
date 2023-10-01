const username = document.querySelector("#username");
const feedBackArea = document.querySelector(".username-feedback");
const email = document.querySelector("#email");
const EmailfeedBackArea = document.querySelector(".email-feedback");
const username_valid = document.querySelector(".username_valid");
const submitBtn = document.querySelector(".submit_btn");

email.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;

  email.classList.remove("text-danger");
  EmailfeedBackArea.style.display = "none";

  if (emailVal.length > 0) {
    fetch("/authentication/validate-email", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.email_error) {
          email.classList.add("text-danger");
          EmailfeedBackArea.style.display = "block";
          EmailfeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
          submitBtn.disabled = true;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});

username.addEventListener("keyup", (e) => {
  console.log("77777", 77777);

  username_valid.style.display = "block";

  const usernameVal = e.target.value;
  username_valid.textContent = `Checking ${usernameVal}`;

  username.classList.remove("text-danger");
  feedBackArea.style.display = "none";

  if (usernameVal.length > 0) {
    fetch("/authentication/validation-username", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        username_valid.style.display = "none";
        if (data.username_error) {
          username.classList.add("text-danger");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
          submitBtn.disabled = true;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});
