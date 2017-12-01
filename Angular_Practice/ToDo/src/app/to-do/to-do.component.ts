import { Component, OnInit } from '@angular/core';

import { TODOS } from '../mocked';

@Component({
  selector: 'app-to-do',
  templateUrl: './to-do.component.html',
  styleUrls: ['./to-do.component.css']
})
export class ToDoComponent implements OnInit {

  todos = TODOS;

  constructor() { }

  ngOnInit() {
  }

}
