import { HttpClientModule, HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CollegeListService {


  constructor(private http:HttpClient) { }

  collegeList(): Observable<any>{
    return this.http.get('http://127.0.0.1:8000/college/api/list/');
  }


}
