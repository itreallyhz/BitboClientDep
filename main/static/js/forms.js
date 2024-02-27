
function showAdditionalFieldsOccupation() {
    var Occupation = document.getElementById("occupation").value;
    var additionalFieldsEmployed = document.getElementById("additionalFieldsEmployed");
    var additionalFieldsStudent = document.getElementById("additionalFieldsStudent");
    var collegeFields = document.getElementById("CollegeFields");

    if (Occupation === "Employed") {
        additionalFieldsEmployed.style.display = "block";
        additionalFieldsStudent.style.display = "none";
        collegeFields.style.display = "none"; // Hide college fields
    } else if (Occupation === "Student") {
        additionalFieldsStudent.style.display = "block";
        additionalFieldsEmployed.style.display = "none";
        toggleFields(); // Call toggleFields only when the occupation is Student
    } else if (Occupation === "College") {
        additionalFieldsEmployed.style.display = "none";
        additionalFieldsStudent.style.display = "none";
        collegeFields.style.display = "block"; // Show college fields
    } else {
        additionalFieldsEmployed.style.display = "none";
        additionalFieldsStudent.style.display = "none";
        collegeFields.style.display = "none"; // Hide college fields for other occupations
    }
}


function toggleFields() {
    var educationLevel = document.getElementById("educational_level").value; // Get the selected value

    // Hide all fields first
    document.getElementById("elementaryFields").style.display = "none";
    document.getElementById("highSchoolFields").style.display = "none";
    document.getElementById("seniorHighSchoolFields").style.display = "none";
    document.getElementById("CollegeFields").style.display = "none";

    // Show the corresponding field based on the selected education level
    if (educationLevel === "Elementary") {
        document.getElementById("elementaryFields").style.display = "block";
    } else if (educationLevel === "High School") {
        document.getElementById("highSchoolFields").style.display = "block";
    } else if (educationLevel === "Senior High School") {
        document.getElementById("seniorHighSchoolFields").style.display = "block";
    } else if (educationLevel === "College") {
        document.getElementById("CollegeFields").style.display = "block";
    }
}

function Ethnicityfunction(){
    
    var indigenous = document.getElementById("is_indigenous").value;
    if (indigenous === "Yes") {
        document.getElementById("indigenousYes").style.display = "block";
    } else{
        document.getElementById("indigenousYes").style.display = "none";
    }
}


function RegisteredVoter(){
    
    var voter = document.getElementById("is_registered_voter").value;
    if (voter === "Yes") {
        document.getElementById("registeredYes").style.display = "block";
    } else{
        document.getElementById("registeredYes").style.display = "none";
    }
}

function PWDfunction(){
    
    var voter = document.getElementById("is_pwd").value;
    if (voter === "Yes") {
        document.getElementById("pwdYes").style.display = "block";
    } else{
        document.getElementById("pwdYes").style.display = "none";
    }
}