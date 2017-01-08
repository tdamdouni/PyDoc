
import ui

class DocsetView (object):
	def __init__(self, docset, types):
		self.data = types
		
	def tableview_did_select(self, tableview, section, row):
		pass
		
	def tableview_number_of_sections(self, tableview):
		return 1
		
	def tableview_number_of_rows(self, tableview, section):
		return len(self.data)
		
	def tableview_cell_for_row(self, tableview, section, row):
		cell = ui.TableViewCell()
		cell.text_label.text = self.data[row]['name']
		cell.accessory_type = 'disclosure_indicator'
		if not self.data[row]['image'] == None:
			cell.image_view.image = self.data[row]['image']
		return cell
	
tv = ui.TableView()
def get_view(docsets, types):
	w,h = ui.get_screen_size()
	tv.width = w
	tv.height = h
	tv.flex = 'WH'
	tv.name = 'PyDoc'
	data = DocsetView(docsets, types)
	tv.delegate = data
	tv.data_source = data
	return tv
