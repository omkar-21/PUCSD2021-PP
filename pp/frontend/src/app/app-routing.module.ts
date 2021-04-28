import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainComponent } from './main/main.component';
import { LoginComponent } from './login/login.component'
import { CollegesComponent } from './colleges/colleges.component';
import { ExamComponent } from './exam/exam.component';
import { NewsComponent } from './news/news.component';
const routes: Routes = [
  {path: '', component: MainComponent},
  {path: 'home', component: LoginComponent},
  {path: 'college', component: CollegesComponent},
  {path: 'exam', component: ExamComponent},
  {path: 'news', component: NewsComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
