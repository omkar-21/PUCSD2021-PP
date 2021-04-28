import { Injectable } from '@angular/core';
import { HttpClientModule, HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ExamListService {


  constructor(private http:HttpClient) { }

  examList(): Observable<any>{
    return this.http.get('http://127.0.0.1:8000/college/api/exam/list/');
  }
  latestExam(): Observable<any>{
    return this.http.get('http://127.0.0.1:8000/college/api/exam/latest');
  }
}
