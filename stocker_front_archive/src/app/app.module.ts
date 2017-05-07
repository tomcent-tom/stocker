import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule, JsonpModule } from '@angular/http';
import { AppComponent } from './components/app/app.component';
import { FeedComponent } from './components/feed/feed.component';
import {FSMAService} from './services/fsma.service';

@NgModule({
  imports: [BrowserModule,
    HttpModule,
    JsonpModule
  ],
  declarations: [AppComponent,
  FeedComponent
  ],
  bootstrap: [AppComponent],
  providers:    [ FSMAService ]
})
export class AppModule { }
