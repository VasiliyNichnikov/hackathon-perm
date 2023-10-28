import typing
import app.core.type_of_garbage_settings as garbage_settings
from ultralytics import YOLO
from ultralytics.engine.results import Results

from app.core.draw_box import draw_box_on_image
from app.core.pathutils import get_weight_path, get_image_path, get_image_path_after_boxing


class GarbageData:
    @property
    def type_of_garbage(self) -> garbage_settings.TypeOfGarbage:
        return self._type_of_garbage

    @property
    def garbage_name(self) -> str:
        return garbage_settings.get_ru_class_by_type(self._type_of_garbage)

    def __init__(self, type_of_garbage: garbage_settings.TypeOfGarbage, count: int) -> None:
        self._type_of_garbage = type_of_garbage
        self._count = count

    def __str__(self) -> str:
        name = self.garbage_name.title()
        return f"{name}: {self._count}"


class GarbageContainer:
    def __init__(self, output_image: str) -> None:
        self._garbage_and_type = {}
        self._output_image: output_image

    def get_number_elements_by_type(self, garbage_type: garbage_settings.TypeOfGarbage) -> int:
        if garbage_type not in self._garbage_and_type.keys():
            print(f"GarbageContainer.get_number_elements_by_type: not found type: {garbage_type}")
            return 0
        return len(self._garbage_and_type[garbage_type])

    def add_garbage(self, garbage: GarbageData) -> None:
        if garbage.type_of_garbage in self._garbage_and_type.keys():
            self._garbage_and_type[garbage.type_of_garbage].append(garbage)
        else:
            self._garbage_and_type[garbage.type_of_garbage] = [garbage]

    def get_fake_garbage_sum_for_view(self) -> typing.Tuple[GarbageData]:
        """
            Это фейковые товары с суммой, использовать только для отображения
        """
        result = []
        for key, values in self._garbage_and_type.items():
            count = len(values)
            result.append(GarbageData(key, count))
        return tuple(result)


class GarbageSearch:

    def __init__(self, name_image: str) -> None:
        self._model: typing.Any = None
        self._name_image = name_image

    def calculate(self) -> GarbageContainer:
        model = self._get_model()

        image_path = get_image_path(self._name_image)
        output_path = get_image_path_after_boxing(self._name_image)
        results: typing.List[Results] = model(image_path)

        container = GarbageContainer(output_path)

        classes = garbage_settings.get_all_eng_classes()
        colors = garbage_settings.get_all_colors()

        for result in results:
            all_idxywh = []
            for j, d in enumerate(result.boxes):
                type_of_garbage = garbage_settings.get_type_by_int_value(int(d.cls))
                idxywh = list(float(element) for element in list(d.xywhn.view(-1)))
                idxywh.insert(0, int(d.cls))
                all_idxywh.append(idxywh)

                garbage_data = GarbageData(type_of_garbage, 1)
                container.add_garbage(garbage_data)

            draw_box_on_image(all_idxywh, classes, colors, image_path, output_path)
        return container

    def _get_model(self) -> typing.Any:
        if self._model is not None:
            return self._model
        weight_path = get_weight_path()
        self._model = YOLO(weight_path)
        self._model.fuse()
        return self._model
