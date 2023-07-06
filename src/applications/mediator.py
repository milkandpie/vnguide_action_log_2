from clean_architecture import EventsMediator

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
