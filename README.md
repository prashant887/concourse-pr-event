# concourse-pr-event

fly -t tutorial set-pipeline -p git-pr-event-pipeline -c pipeline.yml
fly -t tutorial unpause-pipeline -p git-pr-event-pipeline


