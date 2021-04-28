import { Injectable } from '@angular/core';
import { HttpClientModule, HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  constructor(private http:HttpClient) { }
  activateMsgService(userData): Observable<any>{
    const headers = { 'content-type': 'application/json'}  
    const body=JSON.stringify(userData);
    console.log(body)
    return this.http.post('http://localhost:8000/msgservice/api/register/',userData,{'headers':headers});
  }

  logoutUser(userData): Observable<any>{
    return this.http.post('http://127.0.0.1:8000/api/logout/',userData);
  }

  latestnews(): Observable<any>{
    return this.http.get('http://127.0.0.1:8000/news/api/latest/');
  }
  latestexam(): Observable<any>{
    return this.http.get('http://127.0.0.1:8000/college/api/exam/latest/');
  }


}
