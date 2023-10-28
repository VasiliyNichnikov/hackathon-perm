import matplotlib.pyplot as plt

import app.core.type_of_garbage_settings as garbage_settings
from app.core.garbage_search import GarbageSearch, GarbageContainer
from app.core.pathutils import get_chart_path


class ViewData:
    @property
    def chart_path(self) -> str:
        return f"upload/chart/{self._filename}"

    @property
    def box_path(self) -> str:
        return f"upload/box/{self._filename}"

    @property
    def messages(self) -> tuple[str]:
        messages = [str(item) for item in self._container.get_fake_garbage_sum_for_view()]
        return tuple(messages)

    def __init__(self, filename, container: GarbageContainer) -> None:
        self._filename = filename
        self._container = container


class ControllerByDataOutput:
    def __init__(self) -> None:
        self._container: GarbageContainer | None = None

    def get_view_data(self, filename: str) -> ViewData:
        garbage_search = GarbageSearch(filename)
        self._container = garbage_search.calculate()

        labels = []
        counts = []
        for item_type in garbage_settings.TypeOfGarbage:
            self.__add_name_and_count_in_list(item_type, labels, counts)

        self.__save_chart(filename, labels, counts)
        return ViewData(filename, self._container)

    @staticmethod
    def __save_chart(filename: str, labels: list[str], counts: list[int]) -> None:
        chart_path = get_chart_path(filename)
        fig1, ax1 = plt.subplots()
        ax1.pie(counts, labels=labels)
        plt.savefig(chart_path)

    def __add_name_and_count_in_list(self, garbage_type: garbage_settings.TypeOfGarbage, labels_list: list[str],
                                     values_list: list[float]) -> None:
        label = garbage_settings.get_ru_class_by_type(garbage_type)
        count = self._container.get_number_elements_by_type(garbage_type)

        if count == 0:
            return

        labels_list.append(label)
        values_list.append(count)
