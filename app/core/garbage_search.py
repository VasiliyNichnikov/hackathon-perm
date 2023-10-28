import typing

from ultralytics import YOLO
from enum import Enum
from ultralytics.engine.results import Results
from app.core.pathutils import get_weight_path, get_image_path


class TypeOfGarbage(Enum):
    Wood = 0,
    Glass = 1,
    Plastic = 2,
    Metal = 3,
    Unknown = 4


class ResultData:
    def __init__(self, original_image_name: str, type_of_garbage: TypeOfGarbage) -> None:
        self._original_image_name = original_image_name
        self._type_of_garbage = type_of_garbage


class GarbageSearch:

    def __init__(self, name_image: str) -> None:
        self._model: typing.Any = None
        self._name_image = name_image
        self._types_of_garbage = {}

    def calculate(self) -> typing.List[ResultData]:
        model = self._get_model()

        image_path = get_image_path(self._name_image)

        results: typing.List[Results] = model(image_path)

        result_data = []
        for result in results:
            for j, d in enumerate(result.boxes):
                type_of_garbage = TypeOfGarbage.Unknown
                match int(d.cls):
                    case 0:
                        type_of_garbage = TypeOfGarbage.Wood
                    case 1:
                        type_of_garbage = TypeOfGarbage.Glass
                    case 2:
                        type_of_garbage = TypeOfGarbage.Plastic
                    case 3:
                        type_of_garbage = TypeOfGarbage.Metal
                    case _:
                        print(f"GarbageSearch.Calculate: not found class with value: {int(d.cls)}")

                data = ResultData(self._name_image, type_of_garbage)
                result_data.append(data)
        return result_data
            # print(result.to().boxes)
            # print(result.to().keypoints)
            # print(result.to().names)
            # print(result.to().probs[0].cl)
            # result.to().keypoints
            # print(result.to().save_crop(get_image_path(f"test_{number}.png")))

    def _get_model(self) -> typing.Any:
        if self._model is not None:
            return self._model
        weight_path = get_weight_path()
        self._model = YOLO(weight_path)
        self._model.fuse()
        return self._model
