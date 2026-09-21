from bladerunner.core.events import Event, EventKind, Severity
from bladerunner.detectors.rule_based import RuleBasedDetector


def _event(**data) -> Event:
    return Event(kind=EventKind.PROCESS, source="test", agent_id="a1", data=data)


def test_rule_detector_flags_high_cpu() -> None:
    det = RuleBasedDetector()
    v = det.evaluate(_event(cpu_percent=95))
    assert v.is_anomalous
    assert v.severity == Severity.MEDIUM


def test_rule_detector_flags_high_connections() -> None:
    det = RuleBasedDetector()
    v = det.evaluate(_event(connections=150))
    assert v.is_anomalous
    assert v.severity == Severity.HIGH


def test_rule_detector_passes_normal() -> None:
    det = RuleBasedDetector()
    v = det.evaluate(_event(cpu_percent=10, connections=2, open_files=5))
    assert not v.is_anomalous
