const approveButtons = document.querySelectorAll('.approve-button button');

approveButtons.forEach(approveButton => {
  approveButton.addEventListener('click', (e) => {
    e.preventDefault();

    const form = e.target.closest('form');
    const nameofResident = form.querySelector('.name-resident').textContent;
    const date_request = form.querySelector('.date-request').textContent;
    const userEmail = form.querySelector('.user-email').textContent;
    const userId = e.target.getAttribute('data-user-id'); // Assuming you set a 'data-user-id' attribute

    let emailBody = `
      Good Day! Madam/Sir <b>${nameofResident} </b>, we extend our gratitude for requesting Clearances and permit on this day ${date_request} <br>
      Your Request is approved! Please wait for the next information for the next process, Thank you!
    `;

    // Replace 'YOUR_SECURE_TOKEN' with the actual secure token or API key
    Email.send({
      SecureToken: "094b24a6-3cee-4e5f-a3c3-e43b8492ed37",
      To: userEmail,
      From: "bitboph@gmail.com",
      Subject: "BITBO approval",
      Body: emailBody
    })
    .then(() => {
      // Send a GET request to the approval route
      fetch(`/clearance_permit/${userId}`, { method: 'GET' }) // Corrected the endpoint
        .then(response => {
          if (response.ok) {
            // Redirect to the success page after the approval
            window.location.href = '/clearance_permit';
          } else {
            // Handle error response
            console.error('Error approving user');
          }
        });
    })
    .catch(error => {
      // Handle email sending error
      console.error('Error sending email', error);
    });
  });
});


// const approveButtons = document.querySelectorAll('.approve-button button');

// approveButtons.forEach(approveButton => {
//   approveButton.addEventListener('click', (e) => {
//     e.preventDefault();

//     const form = e.target.closest('form');
//     const nameofResident = form.querySelector('.name-resident').textContent;
//     const Request = form.querySelector('.type-request').textContent;
//     const date_request = form.querySelector('.date-request').textContent;
//     const userEmail = form.querySelector('.user-email').textContent;
//     const userId = e.target.getAttribute('data-user-id'); // Assuming you set a 'data-user-id' attribute

//     let emailBody = `
//       Good Day! Madam/Sir <b>${nameofResident} ${Request} ${date_request}</b>, we extend our gratitude for requesting Clearances and permit <br>
//     `;

//     // Replace 'YOUR_SECURE_TOKEN' with the actual secure token or API key
//     Email.send({
//       SecureToken: "4f8d5b81-06e5-43e5-9ba3-c88091d76471",
//       To: userEmail,
//       From: "bitboph@gmail.com",
//       Subject: "BITBO approval",
//       Body: emailBody
//     })
//     .then(() => {
//       // Send a GET request to the approval route
//       fetch(`/clearance_permit/${userId}`, { method: 'GET' }) // Corrected the endpoint
//         .then(response => {
//           if (response.ok) {
//             // Redirect to the success page after the approval
//             window.location.href = 'main/clearance_permit';
//           } else {
//             // Handle error response
//             console.error('Error approving user');
//           }
//         });
//     })
//     .catch(error => {
//       // Handle email sending error
//       console.error('Error sending email', error);
//     });
//   });
// });
