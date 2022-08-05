function validateForm() {
  let username = document.getElementById('username').value;
  let password = document.getElementById('password').value;

  if (username === "") {
      alert('please Enter a Username !');
      return false;

  } else {
      if (password === "") {
        alert('please Enter a Password !');
        return false;
      }     
  }
}