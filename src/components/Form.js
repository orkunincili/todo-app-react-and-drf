import React from 'react';
import '../App.css';
import { FaPlusSquare as Plus } from "react-icons/fa";

const Form = ({inputText,setTodos,todos,setInputText,setStatus}) =>{

  const inputTextHandler =(e)=>{
    console.log(e.target.value);
    setInputText(e.target.value);
  };
  const submitTodoHandler =(e)=>{
    e.preventDefault();
    setTodos([
      ...todos,
      {text:inputText,completed:false,id:Math.random()*1000},
    ]);
    setInputText("");
  };
  const statusHandler =(e)=>{
      setStatus(e.target.value)
  };
  return(

      <form>
        <input value={inputText}  onChange={inputTextHandler} className="todo-input" type="text"/>

          <Plus size={39} onClick={submitTodoHandler}/>

        <select onChange ={statusHandler} name="todos" className="todo-type">
            <option value="all">All</option>
            <option value="completed">Completed</option>
            <option value="uncompleted">Uncompleted</option>

        </select>


      </form>

  );
}

export default Form
