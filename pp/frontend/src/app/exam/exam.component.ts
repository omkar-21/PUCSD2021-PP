import { Component, OnInit } from '@angular/core';
import { ExamListService } from 'src/app/exam/exam-list.service'
@Component({
  selector: 'app-exam',
  templateUrl: './exam.component.html',
  styleUrls: ['./exam.component.css']
})
export class ExamComponent implements OnInit {



  customers ;


  col =[
  {
    field: 'First',
    header: 'Date',
    width: '20%'
  },
  {
    field: 'Second',
    header: 'Exam Name',
    width: '25%'
  },
  {
    field: 'Third',
    header: 'Location',
    width: '45%'
  },
  {
    field: 'Fourth',
    header: 'Apply',
    width: '15%'
  }
]
  first = 0;

  rows = 10;
  constructor(private examlist:ExamListService) { }

  ngOnInit(): void {

    this.examlist.examList().subscribe(
      Response => {
        this.customers = [Response]
        console.log(this.customers)
      },
      error => console.log('error',error)
    );
  }



  next() {
    this.first = this.first + this.rows;
}

prev() {
    this.first = this.first - this.rows;
}

reset() {
    this.first = 0;
}

isLastPage(): boolean {
    return this.customers ? this.first === (this.customers.length - this.rows): true;
}

isFirstPage(): boolean {
    return this.customers ? this.first === 0 : true;
}

}
