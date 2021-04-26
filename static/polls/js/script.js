$('#id_question').ready(function(){
//    question_id = $('#quest_id')[0].textContent;
    question_id = $('#quest_id').text();
    option = document.querySelector('#id_question').getElementsByTagName('option');
    for (let i = 0; i < option.length; i++) {
        if (option[i].value == question_id) option[i].selected = true
    }
})
$('#id_user').ready(function(){
    user_id = $('#user_id').text();
    option = document.querySelector('#id_user').getElementsByTagName('option');
    for (let i = 0; i < option.length; i++) {
        if (option[i].value == user_id) option[i].selected = true;
    }
})