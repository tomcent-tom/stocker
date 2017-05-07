import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule, JsonpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { FeedComponent } from './feed/feed.component';
import { FsmaService } from './fsma.service';
import { SdbService} from './sdb.service';
import { DetailsComponent } from './details/details.component';
import { PortfolioComponent } from './portfolio/portfolio.component';

@NgModule({
  declarations: [
    AppComponent,
    FeedComponent,
    DetailsComponent,
    PortfolioComponent
  ],
  imports: [
    BrowserModule,
    HttpModule,
    JsonpModule
  ],
  providers: [FsmaService, SdbService],
  bootstrap: [AppComponent]
})
export class AppModule { }
