<?php

interface InscriptionIntercae{
    public function getDateCreated(): DateTime;
    public function setDateCreated(DateTime $datetime): void;
}