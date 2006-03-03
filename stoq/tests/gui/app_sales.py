from kiwi.ui.test.player import Player

player = Player(['bin/stoq', 'sales'])
app = player.get_app()

player.wait_for_window("SalesApp")
app.SalesApp.search_button.clicked()
app.SalesApp.filter_combo.select_item_by_label("Reviewing")
app.SalesApp.filter_combo.select_item_by_label("Cancelled")
app.SalesApp.filter_combo.select_item_by_label("Closed")
app.SalesApp.filter_combo.select_item_by_label("Confirmed")
app.SalesApp.filter_combo.select_item_by_label("Opened")
app.SalesApp.filter_combo.select_item_by_label("Any")
app.SalesApp.sales.select_paths(['2'])
app.SalesApp.sales.select_paths(['1'])
app.SalesApp.details_button.clicked()

player.wait_for_window("SaleDetailsDialog")
player.delete_window("SaleDetailsDialog")

app.SalesApp.sales.select_paths(['2'])
app.SalesApp.anytime_check.clicked()
app.SalesApp.date_check.clicked()
app.SalesApp.start_date.set_text("02/20/2006")
app.SalesApp.end_date.set_text("02/20/2006")
app.SalesApp.search_button.clicked()
app.SalesApp.sales.select_paths([])
app.SalesApp.sales.select_paths(['0'])
player.delete_window("SalesApp")

player.finish()
