import React from 'react';
import '../App.css';
import { FaCheck } from "react-icons/fa";
import { BsFillTrash2Fill as Trash } from "react-icons/bs";
const Todo =({todo,todos,setTodos})=>{
  const deleteHandler=()=>{

    setTodos(todos.filter(el=>el.id!==todo.id))
  }
  const completeHandler = ()=>{
    setTodos(todos.map(item=>{
      if(item.id===todo.id){
        return {...item,completed: !item.completed,
        };
      }
      return item;
    }));
  };
  return(
      <div className="todo">
        <li className={`todo-item ${todo.completed ? "completed" : ""}`}>
          {todo.text}
        </li>
        <div className={`${todo.completed ? "check-green" : "check-white"}`}>
            <FaCheck onClick={completeHandler}/>
        </div>
        <div style={{color:'white'}}>
            <Trash onClick={deleteHandler}/>
        </div>

      </div>
  );
};
export default Todo;
