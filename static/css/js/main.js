function check_me(input_id){

    console.log("hi");
    // querySelector() allows users to select first element that matches a given CSS selector
    // it means select the <input> element where id = input_id
    var checked_input = document.querySelector("input[id = " + input_id + "]");
    var checked_label = document.querySelector("label[name = " + input_id + "]");
    // if the item is selected (checked) -> cross the item out of list
    if (checked_input.checked){
        checked_label.style.textDecoration = "line-through";
    }
    // if it's unchecked -> remove the cross line
    else{
        checked_label.style.textDecoration = "";
    }

    var btn = document.getElementById("r_btn");
    // set the text in the btn to remove item
    btn.value = "Remove Items";
    btn.style.color = "#222838";
    btn.style.backgroundColor = "#BBCF9B";
    btn.style.cursor= "pointer";

    
}