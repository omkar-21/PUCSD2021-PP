import { Injectable } from '@angular/core';
import { HttpClientModule, HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NewsListService {


  constructor(private http:HttpClient) { }

  NewsList(): Observable<any>{
    return this.http.get('http://127.0.0.1:8000/news/api/list/');
  }
  latestNews(): Observable<any>{
    return this.http.get('http://127.0.0.1:8000/news/api/latest_news');
  }


}
