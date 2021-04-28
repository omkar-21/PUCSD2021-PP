import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { MainComponent } from './main/main.component';
import { LoginComponent } from './login/login.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import {CardModule} from 'primeng/card';
import {ButtonModule} from 'primeng/button';
import { CollegesComponent } from './colleges/colleges.component';
import {DividerModule} from 'primeng/divider';
import {DataViewModule} from 'primeng/dataview';
import {PanelModule} from 'primeng/panel';
import {DropdownModule} from 'primeng/dropdown';
import {RippleModule} from 'primeng/ripple';
import { ExamComponent } from './exam/exam.component';
import {TableModule} from 'primeng/table';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {FieldsetModule} from 'primeng/fieldset';
import { NewsComponent } from './news/news.component';
import {MenuModule} from 'primeng/menu';
import {MenuItem} from 'primeng/api';
import {ConfirmDialogModule} from 'primeng/confirmdialog';
import {ConfirmationService} from 'primeng/api';
import {MessagesModule, Messages} from 'primeng/messages';
import {MessageModule} from 'primeng/message';
import {MessageService} from 'primeng/api';
import {RatingModule} from 'primeng/rating';
import {DialogModule} from 'primeng/dialog';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    LoginComponent,
    CollegesComponent,
    ExamComponent,
    NewsComponent,

  ],
  imports: [
    RippleModule,
    DialogModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    NgbModule,
    MenuModule,
    ConfirmDialogModule,
    CardModule,
    ButtonModule,
    MessageModule,
    MessagesModule,
    DividerModule,
    DataViewModule,
    DropdownModule,
    PanelModule,
    TableModule,
    BrowserAnimationsModule,
    FieldsetModule,
    RatingModule
    ],
  providers: [ ConfirmationService, MessageService ],
  bootstrap: [AppComponent]
})
export class AppModule { }
