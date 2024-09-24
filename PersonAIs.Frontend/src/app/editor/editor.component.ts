import { Component } from '@angular/core';
import { PdfViewerModule } from 'ng2-pdf-viewer';

@Component({
  selector: 'app-editor',
  standalone: true,
  imports: [PdfViewerModule],
  templateUrl: './editor.component.html',
  styleUrl: './editor.component.scss'
})
export class EditorComponent {
  pdfSrc = "../../assets/Persona.pdf"
}
