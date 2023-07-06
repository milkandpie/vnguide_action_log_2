from clean_architecture import EventsMediator, MediatorGetter as BaseMediatorGetter

from .action_log import ActionLogCreatingCommand, ActionLogCreatingService


class DomainEventMediator(EventsMediator):
    def __init__(self):
        super().__init__({

        })


class CommandEventMediator(EventsMediator):
    def __init__(self):
        super().__init__({
            ActionLogCreatingCommand: [ActionLogCreatingService]
        })


class MediatorGetter(BaseMediatorGetter):
    @staticmethod
    def _create_mediators():
        return {
            'event': DomainEventMediator(),
            'command': CommandEventMediator()
        }
