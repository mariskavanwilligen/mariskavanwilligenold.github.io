Title: Contact
Slug: contact-page

##### **Don't hesitate, get in touch with me!**


<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {font-family: Arial, Helvetica, sans-serif;}
* {box-sizing: border-box;}
input[type=text], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}
input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
input[type=submit]:hover {
  background-color: #45a049;
}
.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>
</head>
<body>

<h3>Contact Form</h3>

<div class="container">
<form name="gform" id="gform" enctype="text/plain" action="https://docs.google.com/forms/d/e/1FAIpQLSccbwkH9WvgAKX-wmjd7P-sSc-wGf85u6HeA5hSpG8oFlAjbA/formResponse?" target="hidden_iframe" onsubmit="submitted=true;">
    <label for="fname">First Name</label>
    <input type="text" id="entry.155443643" name="entry.155443643" placeholder="Your name..">
    <label for="lname">Last Name</label>
    <input type="text" id="entry.1390542618" name="entry.1390542618" placeholder="Your last name..">
    <label for="subject">Subject</label>
    <textarea id="entry.949117067" name="entry.949117067" placeholder="Write something.." style="height:200px"></textarea>
    <label for="email">Email address</label></br>
    <input type="email" name="entry.314564282" id="entry.314564282" placeholder="Your Email address">
    </br>
    </br>
    <input type="submit" value="Send">
  </form>
  <iframe name="hidden_iframe" id="hidden_iframe" style="display:none;" onload="if(submitted) {}"></iframe>
</div>

</body>
</html>

<script src="assets/js/jquery.min.js"></script>
<script type="text/javascript">var submitted=false;</script>
<script type="text/javascript">
$('#gform').on('submit', function(e) {
  $('#gform *').fadeOut(50);
  $('#gform').prepend('Thank You! Your submission has been processed.');
  });
</script>