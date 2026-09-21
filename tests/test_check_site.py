"""Regression tests for the small static checker; Python standard library only."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('check_site',ROOT/'scripts/check_site.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
class SiteChecks(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)/'site';shutil.copytree(ROOT,self.root)
    def tearDown(self): self.tmp.cleanup()
    def mutate(self,old,new):
        p=self.root/'index.html';s=p.read_text();self.assertIn(old,s);p.write_text(s.replace(old,new,1))
    def errors(self): return '\n'.join(module.audit(self.root)[0])
    def test_valid_site(self): self.assertEqual(module.audit(self.root)[0],[])
    def test_broken_anchor(self):
        self.mutate('href="#sk7"','href="#not-a-section"');self.assertIn('Broken internal anchor',self.errors())
    def test_duplicate_id(self):
        self.mutate('id="stack"','id="sk7"');self.assertIn('Duplicate id',self.errors())
    def test_missing_pdf(self):
        (self.root/'assets/Ahn_Sangkyoon_Resume_PythonBackend_Fullstack.pdf').unlink();self.assertIn('Missing local asset',self.errors())
    def test_invalid_pdf(self):
        (self.root/'assets/Ahn_Sangkyoon_Resume_PythonBackend_Fullstack.pdf').write_text('not pdf');self.assertIn('not a PDF',self.errors())
    def test_mutable_source_ref(self):
        p=self.root/'assets/evidence-map.json';p.write_text(p.read_text().replace('ccc66c165eefbdaec77e5bb0cad57b989f38e92c','main'));self.assertIn('Unpinned evidence',self.errors())
    def test_evidence_link_mismatch(self):
        self.mutate('data-evidence="sk7-auth"','data-evidence="sk7-store"');self.assertIn('Evidence URL mismatch',self.errors())
    def test_new_tab_relation(self):
        self.mutate('rel="noopener noreferrer"','rel="nofollow"');self.assertIn('Unsafe new-tab relation',self.errors())
    def test_empty_language(self):
        self.mutate('lang="ko"','lang=""');self.assertIn('language',self.errors())
    def test_missing_image_alt(self):
        self.mutate('</main>','<img src="./favicon.svg"></main>');self.assertIn('Image without alt',self.errors())
    def test_tag_mismatch(self):
        self.mutate('</h1>','</h2>');self.assertIn('Mismatched closing tag',self.errors())
    def test_escape_path(self):
        self.mutate('href="./styles.css"','href="../outside.css"');self.assertIn('Path escapes site',self.errors())
if __name__=='__main__':unittest.main()
