// const spawner = require('child_process').spawn;

// const data_to_pass_in = 'python hai mere bhai';

// console.log('Data sent to python script',data_to_pass_in);
// const python_process = spawner('python',['./student_view.py',data_to_pass_in]);

// python_process.stdout.on('data',(data) => {
//     console.log('Data recieved from python sccript:',data.toString());

// });
  // const usedEnrollmentNumbers = data_to_pass_in ;
  const usedEnrollmentNumbers = ["0901MC211064"] ;
  const enrollmentInput = document.getElementById("enrollmentid");

  enrollmentInput.addEventListener("input", function() {
    const enrollmentNumber = enrollmentInput.value;
    if (usedEnrollmentNumbers.includes(enrollmentNumber)) {
      enrollmentInput.value = ""; // Clear the input field
      alert("Enrollment number is already used.");
      enrollmentInput.disabled = true; // Disable input field
    } else {
      enrollmentInput.disabled = false; // Enable input field
    }
  });
