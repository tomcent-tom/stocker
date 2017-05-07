import { Component, Input} from '@angular/core';
import {Transaction} from '../../assets/transaction';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent{
  @Input() transaction: Transaction;

}
