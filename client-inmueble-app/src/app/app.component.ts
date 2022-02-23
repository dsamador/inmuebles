import { Component } from '@angular/core';
import { AngularFirestore } from '@angular/fire/compat/firestore';
import { NotificationService } from '@app/services';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  showSpinner = false;

  title = 'client-inmueble-app';

  constructor(
    private fs: AngularFirestore
    ,private notification: NotificationService
    )
  { }

  onToggleSpinner() : void {
    this.showSpinner = !this.showSpinner
  }

  onFilesChanged(urls: string | string []) : void {
    console.log('urls', urls);
  }

  onSuccess(): void {
    this.notification.success("El procedimiento fue exitoso");
  }

  onError(): void{
    this.notification.error("Hubo errores en el proceso");
  }
}
