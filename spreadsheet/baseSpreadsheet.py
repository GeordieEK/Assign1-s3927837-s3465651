from spreadsheet.cell import Cell


# -------------------------------------------------
# Base class for spreadsheet implementations. DON'T CHANGE THIS FILE.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# -------------------------------------------------

class BaseSpreadsheet:
    def buildSpreadsheet(self, lCells: [Cell]):  # type: ignore
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        pass

    def appendRow(self) -> bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        pass

    def appendCol(self) -> bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        pass

    def insertRow(self, rowIndex: int) -> bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        pass

    def insertCol(self, colIndex: int) -> bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        pass

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        pass

    def rowNum(self) -> int:
        """
        @return Number of rows the spreadsheet has.
        """

        return 0

    def colNum(self) -> int:
        """
        @return Number of column the spreadsheet has.
        """

        return 0

    def find(self, value: float) -> [(int, int)]:  # type: ignore
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
            """

        pass

    def entries(self) -> [Cell]:  # type: ignore
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        return []
