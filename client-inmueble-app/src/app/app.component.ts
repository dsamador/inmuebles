import { Component } from '@angular/core';
import { AngularFirestore } from '@angular/fire/compat/firestore';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  showSpinner = false;

  title = 'client-inmueble-app';

  constructor(private fs: AngularFirestore) {

  }

  onToggleSpinner() : void {
    this.showSpinner = !this.showSpinner
  }

  onFilesChanged(urls: string | string []) : void {
    console.log('urls', urls);

  }

}
