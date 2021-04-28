import { Component, OnInit } from '@angular/core';
import { NewsListService } from 'src/app/news/news-list.service';
@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {

  constructor( private newsservice:NewsListService) { }
news;
  ngOnInit(): void {
    this.newsservice.NewsList().subscribe(
      Response => {
        this.news = [Response]
      },
      error => console.log('error',error)
    );
  }


}
