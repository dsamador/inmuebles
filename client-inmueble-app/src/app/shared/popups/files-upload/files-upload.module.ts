import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FilesUploadComponent } from './files-upload.component';
import { FilesUploadDirective } from './files-upload.directive';

import { MatDialogModule } from '@angular/material/dialog';

@NgModule({
  declarations: [
    FilesUploadComponent,
    FilesUploadDirective
  ],
  imports: [
    CommonModule,
    MatDialogModule
  ],
  exports: [
    FilesUploadDirective
  ]
})
export class FilesUploadModule { }
