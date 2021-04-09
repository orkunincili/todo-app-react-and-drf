import React from 'react';
import '../App.css';

import Todo from './Todo';

const TodoList = ({todos,setTodos, filteredTodos}) =>{
  
  return(

        <div className="todo-container">
              <ul className="todo-item">
                  {filteredTodos.map(todo=>(
                    <Todo key={todo.id}
                          setTodos={setTodos}
                          todos={todos}
                          todo={todo}
                    />
                  ))}

              </ul>
              <br/>
        </div>

  );
};
export default TodoList;
