document.addEventListener("DOMContentLoaded", function() {
    var currentQuestion = 1;
    var totalQuestions = 10;

    function showQuestion(questionNumber) {
        var currentQuestionElement = document.getElementById('question' + questionNumber);
        currentQuestionElement.style.display = 'block';
    }

    function hideQuestion(questionNumber) {
        var currentQuestionElement = document.getElementById('question' + questionNumber);
        currentQuestionElement.style.display = 'none';
    }

    function showNextQuestion() {
        hideQuestion(currentQuestion);
        currentQuestion++;
        if (currentQuestion <= totalQuestions) {
            showQuestion(currentQuestion);
        } else {
            document.getElementById('submit-button').style.display = 'inline';
        }
    }

    // Show first question initially
    showQuestion(currentQuestion);

    // Add event listeners for the "Next" buttons
    var nextButtons = document.querySelectorAll('.next-button');
    nextButtons.forEach(function(button) {
        button.addEventListener('click', showNextQuestion);
    });
});
