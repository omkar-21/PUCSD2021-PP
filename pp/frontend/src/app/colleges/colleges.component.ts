import { Component, OnInit } from '@angular/core';
import { CollegeListService } from 'src/app/colleges/college-list.service';
import { CommentStmt } from '@angular/compiler';

@Component({
  selector: 'app-colleges',
  templateUrl: './colleges.component.html',
  styleUrls: ['./colleges.component.css']
})
export class CollegesComponent implements OnInit {

  comments:any[];
  constructor(private collegelist:CollegeListService) {}
  ngOnInit(): void {
    
    this.collegelist.collegeList().subscribe(
      Response => {
        this.comments = [Response.data]
        console.log(this.comments)
      },
      error => console.log('error',error)
    );


  }
  sortOrder:any;
  sortField:any;
  car;
  totalRecords=3;
  
  onSortChange(event) {
  let value = event.value;
  
  if (value.indexOf('!') === 0) {
      this.sortOrder = -1;
      this.sortField = value.substring(1, value.length);
  }
  else {
      this.sortOrder = 1;
      this.sortField = value;
  }
  }
  
  

  


}
